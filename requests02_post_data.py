import requests
# 发送post请求,访问tpshop登录接口,提交变单数据(url+data={"keys":"value"})
response = requests.post("http://localhost/index.php?m=Home&c=User&a=do_login",
                         data={"username":"18331559600",
                               "password":"123456",
                               "verify_code":"8888", })
print("登录结果:",response.text)
print("json的结果为:",response.json())
