#!/usr/bin/env python
from argparse import ArgumentParser
from dnacentersdk import api
from dnacentersdk.exceptions import ApiError
import logging
import json
from  time import sleep, time, strftime, localtime
from dnac_config import DNAC, DNAC_USER, DNAC_PASSWORD
import sys
from time import sleep, time
logger = logging.getLogger(__name__)
timeout = 10


def parse_tasks(tasks):
    for steps in tasks['workflow'][0]['steps']:
        print(steps['name'],steps['stepStatus'])

def main(dnac,taskid):
    details = dnac.custom_caller.call_api(method="GET", resource_path=f"api/v1/image/task?taskType=distribute,activate&deviceTaskUuid={taskid}")
    print(json.dumps(details.response,indent=2))
    workflowid = details.response[0].workflowId

    steps = dnac.custom_caller.call_api(method="GET", resource_path=f"api/v1/orchestration-engine/workflow/{workflowid}/TASK_MAJOR")
    print(json.dumps(steps))
    workflows = [ step['tasks'][0]['workflows'][0]['id'] for step in steps['workflow'][0]['steps'] ]
    for workflowid in workflows:
        tasks = dnac.custom_caller.call_api(method="GET", resource_path=f"api/v1/orchestration-engine/workflow/{workflowid}/TASK_MAJOR")
        parse_tasks(tasks)

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
    taskid="cdeb0253-4edb-4441-83a7-9815dc053150"
    taskid='01955ec9-185d-7731-b9e5-95b901fc9224'
    main(dnac,taskid)
