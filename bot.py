import time
import requests
from sqlalchemy import null
import urllib3
import datetime

# variables
api_url = 'https://api.backstage.solutions/api/v1.0/'

# settings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getTokens():
    r = requests.post(api_url + 'Token', json={
        "grant_type": "refresh_token",
        "UserName": "mobilet.default",
        "Password": "mbtX27!",
        "ApiKey": "9BBF0571-BEBF-460D-9317-BDADB5114A6E",
        "FirmCode": "MBT",
        "ChannelCode": "WEB",
        "SubChannelCode": "Mobilet.com"
    }, verify=False)

    return r.json()


def getEvents(access_token, bucket_id):
    r = requests.post(api_url + 'MBT/WEB/ElasticEvent/SearchByBucket', headers={
        'Authorization': 'Bearer ' + access_token,
    }, json={
        "Filter": bucket_id
    }, verify=False)

    return r.json()


last_found_at = None
while True:
    tokens = getTokens()
    bucket = getEvents(tokens['access_token'], 8837)  # 7031 = konusanlar bucket id
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    if len(bucket['ChildEvents']) > 0 and today != last_found_at:
        last_found_at = today
        print('found new event!')
        print(bucket)

    time.sleep(2)
