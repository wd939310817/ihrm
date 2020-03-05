# 封装tpshop的接口
# 获取验证码(令牌)
class Login:
    def __init__(self):
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
    # 封装获取验证码的函数
    def get_verify(self,session):
        response_verify = session.get(self.verify_url)
        return response_verify
        # 封装登陆的函数

    def login(self, session, data):
        response_login = session.post(self.login_url, data=data)
        return response_login