# 对数据库进行封装(emp03)
# 导包
import unittest, logging,apiTestIHRMSystem.app

import pymysql
import requests


# 创建测试类集成unittest.TestCase
from apiTestIHRMSystem.api.emp_api import EmployeeApi
from apiTestIHRMSystem.uitls import assert_common_utils, DBUtils


class TestEmployee(unittest.TestCase):

    # 初始化unittest的函数
    def setUp(self):
        # 实例化EmployeeApi
        self.emp_api = EmployeeApi()

    def tearDown(self):
        pass

    # def login(self, mobile, password):
    #     login_url = "http://182.92.81.159/api/sys/login"
    #     jsonData = {"mobile": mobile, "password": password}
    #     return requests.post(login_url, json=jsonData)


    def test02_login_success(self):
        # 调用登陆
        response = self.emp_api.login("13800000002", "123456")
        # 打印登陆结果
        logging.info("员工模块的登陆结果为：{}".format(response.json()))
        # 取出令牌，并拼接成以Bearer 开头的字符串
        token = "Bearer " + response.json().get('data')
        logging.info("取出的令牌为：{}".format(token))
        # 设置员工模块所需要的请求头
        headers = {"Content-Type": "application/json", "Authorization": token}
        apiTestIHRMSystem.app.HEADERS = headers
        logging.info("员工模块请求头为：{}".format(apiTestIHRMSystem.app.HEADERS))


    def test03_add_emp(self):
        # 调用添加员工
        response_add_emp = self.emp_api.add_emp("王哈哈supperstar04", "18331559003",
                                                apiTestIHRMSystem.app.HEADERS)
        logging.info("添加员工接口的结果为：{}".format(response_add_emp.json()))
        # 由于添加员工成功后，还需要保存员工ID给后续的查询、修改、删除员工使用，所以我们需要保存员工ID
        emp_id = response_add_emp.json().get("data").get("id")
        apiTestIHRMSystem.app.EMPID = emp_id
        logging.info("保存的员工ID为：{}".format(apiTestIHRMSystem.app.EMPID))

        # 建立连接 username：readuser
        # password：iHRM_user_2019
        with DBUtils() as db:
            # 执行SQL语句
            # 根据添加员工返回的id查询数据库中员工表的username，这样就能获取到修改之后的数据
            sql = "select username from bs_user where id = {};".format(apiTestIHRMSystem.app.EMPID)
            logging.info("要查询的SQL语句为：{}".format(sql))
            # 执行查询的sql语句
            db.execute(sql)
            # 获取返回结果
            result = db.fetchone()
            logging.info("SQL查询出来的结果为：{}".format(result))  # ('new_tom',)
            # 断言修改结果是否正确
            # 注意：如果是用fetchall()取出的数据，那么取出result时，需要有两个下标result[0][0]
            self.assertEqual("王哈哈supperstar04", result[0])

        # 断言结果：响应状态码，success，code，message
        assert_common_utils(self, response_add_emp, 200, True, 10000, "操作成功")




    def test04_query_emp(self):
        # 调用查询员工
        response_query = self.emp_api.query_emp(apiTestIHRMSystem.app.EMPID, headers=apiTestIHRMSystem.app.HEADERS)
        logging.info("查询员工的结果为：{}".format(response_query.json()))
        # 断言结果：响应状态码，success，code，message
        assert_common_utils(self, response_query, 200, True, 10000, "操作成功")

    def test05_modify_emp(self):
        # 调用修改员工
        response_modify = self.emp_api.modify_emp(apiTestIHRMSystem.app.EMPID, "new_tom", headers=apiTestIHRMSystem.app.HEADERS)
        logging.info("修改员工结果为：{}".format(response_modify.json()))
        # 断言结果：响应状态码，success，code，message
        assert_common_utils(self, response_modify, 200, True, 10000, "操作成功")

    def test06_delete_emp(self):
        # 调用删除员工
        response_delete = self.emp_api.delete_emp(apiTestIHRMSystem.app.EMPID, apiTestIHRMSystem.app.HEADERS)
        logging.info("删除员工的结果为：{}".format(response_delete.json()))
        # 断言结果：响应状态码，success，code，message
        assert_common_utils(self, response_delete, 200, True, 10000, "操作成功")


