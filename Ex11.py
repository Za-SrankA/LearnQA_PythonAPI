import requests
from requests import Response

response: Response = requests.get(
        "https://playground.learnqa.ru/api/homework_cookie"
    )
print(response.cookies)

assert response.cookies['HomeWork'] == 'hw_value',f"Cookie in response is not correct!!!"