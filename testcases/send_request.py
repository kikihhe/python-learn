import requests as requests

# response = requests.request()
#
# # 响应的字符流数据
# print(response.text)
# # 响应的字节流数据
# print(response.content)
# # 响应的字典数据
# print(response.json())
# # 响应的状态码
# print(response.status_code)


# 发送get请求
# 一共有三个参数，url, params=None, **kwargs
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
