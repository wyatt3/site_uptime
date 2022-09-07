import requests
import os
url = 'https://discord.com/api/webhooks/1016725902140379287/GVIDVseXQrWGClj7x9gyc_VNm-rN_vQnNcMfzprCUfIuW8tsmndqKDQnb1a7FiZLfREk'

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = absolute_path + "/last_check.txt"
last_check = open(file_path, "r")
up = last_check.read()
last_check.close()

try:
    r = requests.head("https://nyoom.wyattjohnson.net", timeout=2.5)
    print(r.status_code)
    if r.status_code == 200 and up != "true":
        this_check = open(file_path, "w")
        this_check.write("true")
        this_check.close()

        message = {
            "content": "Nyoom is back up",
            "username": "Uptime Checkorator",
            "avatar_url": "https://i.imgur.com/M3z7bgZ.gif"
        }
        requests.post(url, json = message)
except:
    print('site is down')
    if up == "true":
        print('send message')
        this_check = open(file_path, "w")
        this_check.write("false")
        this_check.close()

        message = {
            "content": "Nyoom is borked",
            "username": "Downtime Checkorator",
            "avatar_url": "https://i.imgur.com/sohWhy9.png"
        }
        requests.post(url, json = message)
