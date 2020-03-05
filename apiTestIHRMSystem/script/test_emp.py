# 员工模块增删改查用例
# 导包
import unittest, logging,apiTestIHRMSystem.app
import requests


# 创建测试类集成unittest.TestCase
class TestEmployee(unittest.TestCase):

    # 初始化unittest的函数
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 创建测试函数

    def test01_emp_management(self):
        # 初始化日志
        apiTestIHRMSystem.app.init_logging()
        # 调用登陆
        response = requests.post("http://182.92.81.159/api/sys/login",
                                 json={"mobile": "13800000002", "password": "123456"})
        # 打印登陆结果
        logging.info("员工模块的登陆结果为：{}".format(response.json()))
        # 取出令牌，并拼接成以Bearer 开头的字符串
        token = "Bearer " + response.json().get('data')
        logging.info("取出的令牌为：{}".format(token))
        # 设置请求头
        headers = {"Content-Type": "application/json", "Authorization": token}
        logging.info("员工模块请求头为：{}".format(headers))
        # 调用添加员工
        response_add_emp = requests.post("http://182.92.81.159/api/sys/user",
                                         json={"username": "王哈哈supperstar04",
                                               "mobile": "18331559003",
                                               "timeOfEntry": "2020-02-01",
                                               "formOfEmployment": 1,
                                               "departmentName": "酱油2部",
                                               "departmentId": "1205026005332635648",
                                               "correctionTime": "2020-02-03T16:00:00.000Z"},
                                         headers=headers)
        logging.info("1.添加员工接口的结果为：{}".format(response_add_emp.json()))
        # 断言结果：响应状态码，success，code，message
        self.assertEqual(200, response_add_emp.status_code)
        self.assertEqual(True, response_add_emp.json().get("success"))
        self.assertEqual(10000, response_add_emp.json().get("code"))
        self.assertIn("操作成功", response_add_emp.json().get("message"))


        # 查询员工id
        emp_id = response_add_emp.json().get("data").get("id")
        logging.info("保存的员工id为：{}".format(emp_id))
        # 调用查询员工
        query_url = "http://182.92.81.159/api/sys/user/" + emp_id
        response_query = requests.get(query_url,headers=headers)
        logging.info("2.查询的员工id为：{}".format(response_query.json()))
        # 断言结果：响应状态码，success，code，message
        self.assertEqual(200, response_query.status_code)
        self.assertEqual(True, response_query.json().get("success"))
        self.assertEqual(10000, response_query.json().get("code"))
        self.assertIn("操作成功", response_query.json().get("message"))


        # 调用修改员工
        modify_url = "http://182.92.81.159/api/sys/user/"  + emp_id
        response_modify = requests.put(modify_url,
                                       json={"username": "王嘻哈supperstar04"},
                                       headers=headers)
        logging.info("3.修改员工结果为：{}".format(response_modify.json()))
        # 断言结果：响应状态码，success，code，message
        self.assertEqual(200, response_modify.status_code)
        self.assertEqual(True, response_modify.json().get("success"))
        self.assertEqual(10000, response_modify.json().get("code"))
        self.assertIn("操作成功", response_modify.json().get("message"))


        # 调用删除员工
        delete_url = "http://182.92.81.159/api/sys/user/"  + emp_id
        response_delete = requests.delete(delete_url, headers=headers)
        logging.info("4.删除员工的结果为：{}".format(response_delete.json()))
        # 断言结果：响应状态码，success，code，message
        self.assertEqual(200, response_delete.status_code)
        self.assertEqual(True, response_delete.json().get("success"))
        self.assertEqual(10000, response_delete.json().get("code"))
        self.assertIn("操作成功", response_delete.json().get("message"))