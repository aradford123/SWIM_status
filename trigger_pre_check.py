#!/usr/bin/env python
from argparse import ArgumentParser
from dnacentersdk import api
from dnacentersdk.exceptions import ApiError
import logging
import json
from  time import sleep, time, strftime, localtime
from dnac_config import DNAC, DNAC_USER, DNAC_PASSWORD
import sys
logger = logging.getLogger(__name__)
timeout = 10

class TaskTimeoutError(Exception):
    pass

class TaskError(Exception):
    pass

def wait_for_task(dnac, taskid, retry=2, timeout=10):
    start_time = time()
    first = True
    while True:
        result = dnac.task.get_task_by_id(taskid)

        # print json.dumps(response)
        if result.response.endTime is not None:
            return result
        else:
            # print a message the first time throu
            if first:
                logger.debug("Task:{} not complete, waiting {} seconds, polling {}".format(taskid, timeout, retry))
                first = False
            if timeout and (start_time + timeout < time()):
                raise TaskTimeoutError("Task %s did not complete within the specified timeout "
                                       "(%s seconds)" % (taskid, timeout))

            logging.debug("Task=%s has not completed yet. Sleeping %s seconds..." % (taskid, retry))
            sleep(retry)

        if result.response.isError == "True":
            raise TaskError("Task %s had error %s" % (taskid, result.response.progress))

    return response


def main(dnac,deviceid):
    payload = ["16c6b215-f29f-4586-b6d9-dd76bbd525cf"]

    details = dnac.custom_caller.call_api(method="POST", data=json.dumps(payload),resource_path=f"api/v1/image/upgrade-analysis")
    print(json.dumps(details.response,indent=2))

    # there will be task that needs to be polled.
    taskid = details.response.taskId
    result = wait_for_task(dnac,taskid)
    
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    parser = ArgumentParser(description='Select options.')
    parser.add_argument('-v', action='store_true',
                        help="verbose")
    parser.add_argument('--password',  type=str, required=False,
                        help='new passowrd')
    parser.add_argument('--dnac',  type=str,default=DNAC,
                        help='dnac IP')
    args = parser.parse_args()

    if args.v:
        root_logger=logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        root_logger.addHandler(ch)
        logger.debug("logging enabled")

    #logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    DNAC = args.dnac
    dnac = api.DNACenterAPI(base_url='https://{}:443'.format(DNAC),
                                #username=DNAC_USER,password=DNAC_PASSWORD,verify=False,debug=True)
                                username=DNAC_USER,password=DNAC_PASSWORD,verify=False)
    deviceid='2e4c1316-9d0e-4945-a041-b9b746d304cb'
    deviceid='3b469f1c-7ba0-4fd5-9c8a-4855366bf2eb'
    main(dnac,deviceid)
