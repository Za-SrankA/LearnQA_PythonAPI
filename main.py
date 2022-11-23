
import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

print(f"Кол-во редиректов: {len(response.history)}")
print(f"Последний URL: {response.url}")
