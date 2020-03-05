import requests
# 需求：完成TPSHOP的登陆并登陆成功，然后再登陆成功之后，访问我的订单页面
# （注意，如果没有登陆成功，那么访问我的订单页面时，会跳转到登陆页面）
"""
获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
登录：http://localhost/index.php?m=Home&c=User&a=do_login
我的订单：http://localhost/Home/Order/order_list.html
"""
# 发送获取验证码的接口请求
response_verify = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
# 获取cookie数据
cookies = response_verify.cookies
#  调用登陆接口，把cookies发送给服务器（由于在tpshop项目中，令牌会存储到cookies中，所有发送cookies相当于发送了令牌）
response_login = requests.post("http://localhost/index.php?m=Home&c=User&a=do_login",
                         data={"username":"18331559600",
                               "password":"123456",
                               "verify_code":"8888", },cookies=cookies)
print("登录结果:",response_login.json())
# 调用我的订单页面，查看订单信息
# 注意：令牌的作用是用来维持登陆状态的，如果我们不把令牌传递给服务器，服务器就会认为我们的访问是一个新的访问
# 这样，就会导致访问登陆后的页面操作时，服务器让我们跳转到登陆页面
response_order = requests.get("http://localhost/Home/Order/order_list.html",cookies=cookies)
print("我的订单:",response_order.text)