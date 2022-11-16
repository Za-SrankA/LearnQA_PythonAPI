import requests
import time

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

token = response1.json()['token']

param = {'token': token}
status1 = "Job is NOT ready"

response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=param)

if response2.json()['status'] == status1:
    print(f"До ожидания статус правильный")
else:
    print(f"До ожидания статус неправильный")

wait_time = response1.json()['seconds']
status2 = "Job is ready"

time.sleep(wait_time)
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=param)

if response3.json()['status'] == status2:
    print(f"После ожидания статус правильный")
else:
    print(f"После ожидания статус неправильный")

print(response3.text)