# SoftWare Image Management (SWIM) status
These two utilities allow access to specific SWIM API.  

*** warning:  these are internal API, and the public ones will be available Mid 2025

## Getting stated
First (optional) step, create a vitualenv. This makes it less likely to clash with other python libraries in future.
Once the virtualenv is created, need to activate it.
```buildoutcfg
python3 -m venv env3
source env3/bin/activate
```

Next clone the code.

```buildoutcfg
git clone https://github.com/aradford123/mapsiteSSID.git
```

Then install the  requirements (after upgrading pip). 
Older versions of pip may not install the requirements correctly.
```buildoutcfg
pip install -U pip
pip install -r requirements.txt
```

Edit the dnac_vars file to add your DNAC and credential.  You can also use environment variables.

## Credentials

You can either add environment variables, or edit the  dnac_config.py file
```
import os
DNAC= os.getenv("DNAC") or "sandboxdnac.cisco.com"
DNAC_USER= os.getenv("DNAC_USER") or "devnetuser"
DNAC_PORT=os.getenv("DNAC_PORT") or 8080
DNAC_PASSWORD= os.getenv("DNAC_PASSWORD") or "Cisco123!"
```

## trigger_pre_check.py
This script will trigger a pre-check on a given device.

### Example
```
./trigger_pre_check.py 
{
  "taskId": "0195a168-fdea-7737-838f-d948efa0ec7f",
  "url": "/api/v1/task/0195a168-fdea-7737-838f-d948efa0ec7f"
}
{
  "response": {
    "startTime": 1742169767402,
    "progress": "Swim Network Validation Successfully Executed",
    "version": 1742169772256,
    "endTime": 1742169772256,
    "serviceType": "Swim Service",
    "isError": false,
    "instanceTenantId": "5d817bf369136f00c74cb23b",
    "id": "0195a168-fdea-7737-838f-d948efa0ec7f"
  },
  "version": "1.0"
}


```
## dump_pre_check.py
This script will dump the readiness checks for a device.  It takes a device UUID.

### Example

```
/dump_pre_check.py 
[
  {
    "namespace": "image-management",
    "resultTaskUuid": "5317ba73-4ebe-4902-b9cf-133c126c2e7b",
    "parentTaskUuid": "019568f8-58d0-74ae-bd36-b28e4adc7b61",
    "validationBindingUuid": "8a791f0b-d142-48b0-9477-ebf1bd16cd6c",
    "validatorUuid": "1cf68bf1-cce4-484d-b392-484a7fbf329c",
    "validatorName": "Startup config check",
    "validatorType": "XDE",
    "operationName": "upgrade-analysis",
    "typeName": "PRE",
    "statusCode": "1000",
    "resultStatus": "SUCCESS",
    "detail": "Startup config check: SUCCESS",
    "createdTime": 1741222861206,
    "updatedTime": 1741222864100,
    "deviceUuid": "2e4c1316-9d0e-4945-a041-b9b746d304cb",
    "deviceIpAddress": "10.10.15.200",
    "hostName": "3k-stack",
    "resultDetail": [
      {
        "key": "actual",
        "value": "",
        "displayName": "Actual"
      },
      {
        "key": "expected",
        "value": "",
        "displayName": "Expected"
      },
      {
        "key": "description",
        "value": "Startup configuration exist for this device",
        "displayName": "Description"
      },
      {
        "key": "action",
        "value": "",
        "displayName": "Action"
      },
      {
        "key": "status",
        "value": "success",
        "displayName": "Status"
      }
    ]
  },
  {
    "namespace": "image-management",
    "resultTaskUuid": "5c77e172-e8ee-493e-bc93-03ea4060dae0",
    "parentTaskUuid": "019568f8-58d0-74ae-bd36-b28e4adc7b61",
    "validationBindingUuid": "eca2b4c1-ea3b-4609-9020-876d8fe59734",
    "validatorUuid": "e1bbcf15-20bc-4a6f-8a06-e59181de84f4",
    "validatorName": "Config register check",
    "validatorType": "XDE",
    "operationName": "upgrade-analysis",
    "typeName": "PRE",
    "statusCode": "1000",
    "resultStatus": "SUCCESS",
    "detail": "Config register check: SUCCESS",
    "createdTime": 1741222861161,
    "updatedTime": 1741222863699,
    "deviceUuid": "2e4c1316-9d0e-4945-a041-b9b746d304cb",
    "deviceIpAddress": "10.10.15.200",
    "hostName": "3k-stack",
    "resultDetail": [
      {
        "key": "actual",
        "value": "0x102",
        "displayName": "Actual"
      },
      {
        "key": "expected",
        "value": "0x2102,0x102",
        "displayName": "Expected"
      },
      {
        "key": "description",
        "value": "Config-register verified successfully",
        "displayName": "Description"
      },
      {
        "key": "action",
        "value": "No action required",
        "displayName": "Action"
      },
      {
        "key": "status",
        "value": "success",
        "displayName": "Status"
      }
    ]
  },
  {
    "namespace": "image-management",
    "resultTaskUuid": "83b56877-7c3f-49a9-a538-0cc840d414bd",
    "parentTaskUuid": "019568f8-58d0-74ae-bd36-b28e4adc7b61",
    "validationBindingUuid": "c40a42b0-7a33-49f0-8392-9cdabb8c936a",
    "validatorUuid": "902c5485-9b16-4577-839b-c31ee34b4a84",
    "validatorName": "Flash check",
    "validatorType": "JAVA_BEAN",
    "operationName": "upgrade-analysis",
    "typeName": "PRE",
    "statusCode": "1000",
    "resultStatus": "WARNING",
    "detail": "Flash check: WARNING",
    "createdTime": 1741222861128,
    "updatedTime": 1741222862906,
    "deviceUuid": "2e4c1316-9d0e-4945-a041-b9b746d304cb",
    "deviceIpAddress": "10.10.15.200",
    "hostName": "3k-stack",
    "resultDetail": [
      {
        "key": "actual",
        "value": "flash: 471 MB",
        "displayName": "Actual"
      },
      {
        "key": "expected",
        "value": "1005 MB\n Available Free space is: 471 MB [Install mode needs free space to 2.2 times of Image size]",
        "displayName": "Expected"
      },
      {
        "key": "action",
        "value": "Please Clean the Flash location And then Resync the device. However flow can proceed, auto flash clean up will be attempted for this device.",
        "displayName": "Action"
      },
      {
        "key": "description",
        "value": "Image Size is larger than free space",
        "displayName": "Description"
      },
      {
        "key": "status",
        "value": "WARNING",
        "displayName": "Status"
      }
    ]
  },
<SNIP>
```
