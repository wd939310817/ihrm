import requests
# 发送post请求,对ihrm系统的登录接口进行的访问(访问的数据是json格式的数据)
response = requests.post("http://182.92.81.159/api/sys/login",json={"mobile":"13800000002",
                                                                    "password":"123456"})
print("IHRM登录结果:{}".format(response.json()))
# print("IHRM登录结果:",response.json())