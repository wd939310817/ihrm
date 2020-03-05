# 部门模块 进行封装
# 导包
import unittest, logging,apiTestIHRMSystem.app
import requests


# 创建测试类集成unittest.TestCase
from apiTestIHRMSystem.api.emp_api import EmployeeApi
from apiTestIHRMSystem.uitls import assert_common_utils


class TestEmployee(unittest.TestCase):

    # 初始化unittest的函数
    def setUp(self):
        # 实例化EmployeeApi
        self.emp_api = EmployeeApi()

    def tearDown(self):
        pass

    # 创建测试函数

    def test01_emp_management(self):

        # 调用登陆
        response = self.emp_api.login("13800000002", "123456")
        # 打印登陆结果
        logging.info("员工模块的登陆结果为：{}".format(response.json()))
        # 取出令牌，并拼接成以Bearer 开头的字符串
        token = "Bearer " + response.json().get('data')
        logging.info("取出的令牌为：{}".format(token))
        # 设置请求头
        headers = {"Content-Type": "application/json", "Authorization": token}
        logging.info("部门模块请求头为：{}".format(headers))


        # 调用添加员工
        response_add_emp = self.emp_api.add_emp("王哈哈supperstar04","18331559003",headers)
        logging.info("1.添加员工接口的结果为：{}".format(response_add_emp.json()))
        # 断言结果：响应状态码，success，code，message
        assert_common_utils(self,response_add_emp,200,True,10000,"操作成功")


        # 查询员工id
        emp_id = response_add_emp.json().get("data").get("id")
        logging.info("保存的员工id为：{}".format(emp_id))
        # 调用查询员工
        response_query = self.emp_api.query_emp(emp_id, headers=headers)
        logging.info("2.查询的员工id为：{}".format(response_query.json()))
        # 断言结果：响应状态码，success，code，message
        assert_common_utils(self, response_query, 200, True, 10000, "操作成功")


        # 调用修改员工
        response_modify = self.emp_api.modify_emp(emp_id, "王嘻哈supperstar04", headers=headers)
        logging.info("3.修改员工结果为：{}".format(response_modify.json()))
        # 断言结果：响应状态码，success，code，message
        assert_common_utils(self, response_modify, 200, True, 10000, "操作成功")


        # 调用删除员工
        response_delete = self.emp_api.delete_emp(emp_id, headers=headers)
        logging.info("4.删除员工的结果为：{}".format(response_delete.json()))
        # 断言结果：响应状态码，success，code，message
        assert_common_utils(self, response_delete, 200, True, 10000, "操作成功")

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
            response_add_emp = self.emp_api.add_emp("王哈哈supperstar04","18331559003",
                                                    apiTestIHRMSystem.app.HEADERS)
            logging.info("添加员工接口的结果为：{}".format(response_add_emp.json()))
            # 断言结果：响应状态码，success，code，message
            assert_common_utils(self, response_add_emp, 200, True, 10000, "操作成功")