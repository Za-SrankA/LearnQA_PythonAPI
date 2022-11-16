import requests

correct_params = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]

for param in correct_params:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
    print(f"Метод GET c параметром {param} возвращает статус-код {response.status_code} с текстом {response.text}")

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
    print(f"Метод POST c телом {param} возвращает статус-код {response.status_code} с текстом {response.text}")

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
    print(f"Метод PUT c телом {param} возвращает статус-код {response.status_code} с текстом {response.text}")

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
    print(f"Метод DELETE c телом {param} возвращает статус-код {response.status_code} с текстом {response.text}")
