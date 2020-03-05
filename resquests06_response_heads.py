import requests
# 设置请求头
headers = {"Content-Type":"applocation/json"}
# 发送post请求
response = requests.post("http://182.92.81.159/api/sys/login",json={"mobile":"13800000002",
                         "password":"123456"},
                         headers=headers)
print("结果:",response.json())