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


def main(dnac,deviceid):
    details = dnac.custom_caller.call_api(method="GET", resource_path=f"api/v1/validation/result?deviceUuIds={deviceid}&namespace=image-management&typeName=PRE&operationName=upgrade-analysis&latestValidation=true&sortOrder=des")
    print(json.dumps(details.response,indent=2))

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
    main(dnac,deviceid)
