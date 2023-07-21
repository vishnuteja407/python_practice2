import requests
import json

url = "https://10.10.10.101/dna/intent/api/v1/network-device-poller/cli/read-request"

payload = json.dumps({
  "commands": [
    "show interface status",
    "show interface trunk",
    "show vlan",
    "show cdp neighbors",
    "show run"
  ],
  "deviceUuids": [
    "35cdc38d-160e-4c5d-a020-3db09f8f07dd"
  ]
})
headers = {
  'x-auth-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWVmODU4MWRkZTRjZjE4NjA1MWUxODQiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYxZWY4NTgwZGRlNGNmMTg2MDUxZTE4MyJdLCJ0ZW5hbnRJZCI6IjYxZWY4NTdmZGRlNGNmMTg2MDUxZTE4MSIsImV4cCI6MTY4OTI2ODc2MSwiaWF0IjoxNjg5MjY1MTYxLCJqdGkiOiI2MjkzZTBkNS1jNDZkLTQ0NGYtOWM1OC0wMjRkOThhNDhmNTQiLCJ1c2VybmFtZSI6ImFkbWluIn0.VFWPY-cFtizTTMOahcmOgHt3ShMsrgdZKkd2nwwO3kdVrjaYs_aP1WWVisM0WgqvASayl62G53FLp0sCsbXVLYR9QT-zzKGisgPwCxeAmBaH7wsHUskSdo5O9aUqTUCp4EayYi_CQMhj3UqGZIXqK_zKCHCuIHnbeQLkXSyxBby9LG_9K6GxmpdyK_TOr1rsT-378EpBQegXzgBklO1epwekMGCPI7ufBzmqlcJ8x2jZyIOZjlM7xm4xJGDZwXl_J1w8KQLXihjsXAcOT4L9DTwSymtSbyqRLXlbL5L7YXK8Hl4FyyS3VatBuEfVEcbBhpJ6gBsnM34XtaD1fMyEMg',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
