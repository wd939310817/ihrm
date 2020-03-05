import unittest ,requests
from selenium import webdriver
class TestTpshopLogin(unittest.TestCase):
    def setUp(self):
        # 实例化session
        self.session = requests.Session()
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login = "http://localhost/index.php?m=Home&c=User&a=do_login"
        # driver = webdriver.Chrome()
    def tearDown(self):
        self.session.close()
    def test_toshop_login01(self):

       # 调用获取验证码接口
        response_verify = self.session.get(self.verify_url)
        # 打印验证码接口返回的响应头
        print("验证码接口返回的响应头:",response_verify.headers)
        # 断言响应头当中的Content-Type的值是不是一个image/png
        self.assertIn("image/png",response_verify.headers.get("Content-Type"))
        # 使用session实例送登陆接口,session会自动把保存的令牌发送给服务器
        response_login =self.session.post(self.login,
                                      data={"username": "18331559600",
                                            "password": "123456",
                                            "verify_code": "8888", })
        # 打印登陆接口返回的响应数据
        jsonData = response_login.json()#type:dict
        print("登录结果:", response_login.json())
        # 断言响应状态码、响应json数据当中的status的值和msg的值
        self.assertEqual(200,response_login.status_code)
        self.assertEqual(1,jsonData.get("status"))
        self.assertIn("登陆成功",jsonData.get("msg"))

    def test_toshop_login02(self):

       # 调用获取验证码接口
        response_verify = self.session.get(self.verify_url)
        # 打印验证码接口返回的响应头
        print("验证码接口返回的响应头:",response_verify.headers)
        # 断言响应头当中的Content-Type的值是不是一个image/png
        self.assertIn("image/png",response_verify.headers.get("Content-Type"))
        # 使用session实例送登陆接口,session会自动把保存的令牌发送给服务器
        response_login =self.session.post(self.login,
                                      data={"username": "17331559600",
                                            "password": "123456",
                                            "verify_code": "8888", })
        # 打印登陆接口返回的响应数据
        jsonData = response_login.json()#type:dict
        print("登录结果:", response_login.json())
        # 断言响应状态码、响应json数据当中的status的值和msg的值
        self.assertEqual(200,response_login.status_code)
        self.assertEqual(-1,jsonData.get("status"))
        self.assertIn("账号不存在",jsonData.get("msg"))

    def test_toshop_login03(self):

       # 调用获取验证码接口
        response_verify = self.session.get(self.verify_url)
        # 打印验证码接口返回的响应头
        print("验证码接口返回的响应头:",response_verify.headers)
        # 断言响应头当中的Content-Type的值是不是一个image/png
        self.assertIn("image/png",response_verify.headers.get("Content-Type"))
        # 使用session实例送登陆接口,session会自动把保存的令牌发送给服务器
        response_login =self.session.post(self.login,
                                      data={"username": "18331559600",
                                            "password": "1234526",
                                            "verify_code": "8888", })
        # 打印登陆接口返回的响应数据
        jsonData = response_login.json()#type:dict
        print("登录结果:", response_login.json())
        # 断言响应状态码、响应json数据当中的status的值和msg的值
        self.assertEqual(200,response_login.status_code)
        self.assertEqual(-2,jsonData.get("status"))
        self.assertIn("密码错误",jsonData.get("msg"))







