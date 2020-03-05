import requests
# 发送查询天气的接口请求
response = requests.get("http://www.weather.com.cn/data/sk/101010100.html")
print("响应json数据:",response.json())
# 查看编码
print("编码:",response.encoding)
#解决方式1
response.encoding = "utf-8"
print("设置编码后响应json数据:",response.json())
# 解决方式2
print("通过字节码重新编码:",response.content.decode(encoding="utf-8"))