import requests

class TestExample12:

    def test_header(self):
        response = requests.post(
            "https://playground.learnqa.ru/api/homework_header"
        )
        print(response.headers)
        x_s_h_h = response.headers['x-secret-homework-header']
        excepted_result = "Some secret value"

        assert x_s_h_h == excepted_result,f"The 'x-secret-homework-header' in is not correct! Now:{x_s_h_h}"