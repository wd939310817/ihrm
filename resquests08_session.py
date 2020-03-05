# 需求:完成TPSHOP登陆成功操作，并访问我的订单页面
# 要求使用session来完成
import requests
"""
获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
登录：http://localhost/index.php?m=Home&c=User&a=do_login
我的订单：http://localhost/Home/Order/order_list.html
"""
# 初始化session实例
session =requests.Session()
# # 使用session实例发送获取验证码的接口请求  session会自动管理获取验证码接口返回的令牌
response = session.get("http://localhost/index.php?m=Home&c=User&a=verify")
# 使用session实例送登陆接口,session会自动把保存的令牌发送给服务器
response_login = session.post("http://localhost/index.php?m=Home&c=User&a=do_login",
                         data={"username":"18331559600",
                               "password":"123456",
                               "verify_code":"8888", })
print("登录结果:",response_login.json())
# 使用session实例发送我的订单页面接口请求,查看订单信息
response_order = session.get("http://localhost/Home/Order/order_list.html")
print("我的订单:",response_order.text)
# 关闭session
session.close()