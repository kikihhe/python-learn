import requests


class TestSendRequest:
    def test_getResponse(selfself):
        url = "http://localhost:8081/user/test"
        data = {
            "name": "小明"
        }
        response = requests.get(url, data)
        print("响应json", response.json())
        print("响应字符串", response.text)
        print("响应码", response.status_code)
        print("响应字节流数据", response.content)

        print("响应的message信息", response.json()['message'])
        print("响应码", response.json()['code'])

