# 导包
import requests


# 创建API类
class EmployeeApi:
    def __init__(self):
        pass

    # 实现封装登陆接口
    def login(self, mobile, password):
        login_url = "http://182.92.81.159/api/sys/login"
        jsonData = {"mobile": mobile, "password": password}
        return requests.post(login_url, json=jsonData)
    # 实现封装添加员工接口

    def add_dep(self,username,monile,headers):
        add_dep_url = "http://182.92.81.159/api/sys/user"
        jsonData ={"username": "王哈哈supperstar04",
                                               "mobile": "18331559003",
                                               "timeOfEntry": "2020-02-01",
                                               "formOfEmployment": 1,
                                               "departmentName": "酱油2部",
                                               "departmentId": "1205026005332635648",
                                               "correctionTime": "2020-02-03T16:00:00.000Z"
                          }
        return requests.post(add_dep_url,json=jsonData,headers=headers)

    # 封装查询员工接口
    def query_dep(self, emp_id, headers):
        query_url = "http://182.92.81.159/api/sys/user/" + emp_id
        return requests.get(query_url, headers=headers)

    # 封装修改员工接口
    def modify_dep(self, emp_id, username, headers):
        modify_url = "http://182.92.81.159/api/sys/user/"+ emp_id
        return requests.put(modify_url, json={"username": username}, headers=headers)

    # 封装删除员工接口
    def delete_dep(self, emp_id, headers):
        delete_url = "http://182.92.81.159/api/sys/user/"  + emp_id
        return requests.delete(delete_url, headers=headers)

