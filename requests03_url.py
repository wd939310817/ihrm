import requests
# 发送get请求,访问百度搜索接口,查询参数:wd=Python
# 1.把查询参数写在url中:
response_url = requests.get("http://www.baidu.com/s?wd=python")
print("url结果为:",response_url.text)
# 2.把查询参数写在params参数q中,param设置为字符串
response_params_string = requests.get("http://www.baidu.com/s",params="wd=啊哈哈")
print("params_string结果为:",response_params_string.text)
# 3.把查询参数写在params参数q中,param设置为字典
response_params_dict = requests.get("http://www.baidu.com/s",params={"wd":"哒哒哒"})
print("params_dict结果为:",response_params_dict.text)
