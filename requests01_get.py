import requests
# 发送get请求
response = requests.get("http://www.baidu.com")
# 打印text文本内容
print(response.text)