import requests
r = requests.head("https://nyoom.wyattjohnson.net")

url = 'https://discord.com/api/webhooks/1016725902140379287/GVIDVseXQrWGClj7x9gyc_VNm-rN_vQnNcMfzprCUfIuW8tsmndqKDQnb1a7FiZLfREk'

last_check = open(r"last_check.txt", "r")
up = last_check.read()
last_check.close()

if r.status_code == 200 and up != "true":
    message = {
        "content": "Nyoom is back up",
        "username": "Uptime Checkorator",
        "avatar_url": "https://i.imgur.com/M3z7bgZ.gif"
    }
    this_check = open(r"last_check.txt", "w")
    this_check.write("true")
    requests.post(url, json = message)
elif r.status_code != 200 and up == "true":
    message = {
        "content": "Nyoom is borked",
        "username": "Downtime Checkorator",
        "avatar_url": "https://i.imgur.com/sohWhy9.png"
    }
    this_check = open(r"last_check.txt", "w")
    this_check.write("false")
    requests.post(url, json = message)
