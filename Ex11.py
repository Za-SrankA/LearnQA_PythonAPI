import requests
class TestExample11:
    def test_cookie(self):
        response = requests.post(
            "https://playground.learnqa.ru/api/homework_cookie"
        )
        print(response.cookies)

        excepted_result = "hw_value"
        assert response.cookies['HomeWork'] == excepted_result,f"Cookie in response is not correct! Now: {response.cookies['HomeWork']}"