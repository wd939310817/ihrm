import requests
# 发送请求
response = requests.get("http://www.baidu.com")
# 1.获取响应状态码:状态码中的数据
http_stayus = response.status_code
print("响应状态码:",http_stayus)
# 2.获取请求url
requests_url = response.url
print("请求url:",requests_url)
# 3.获取响应字符编码  ISO-8859-1默认编码(国际)
encode2 = response.encoding
print("响应字符编码:",encode2)
# 4.获取响应头数据
headers = response.headers
print("响应头数据:",headers)
# 5.获取响应的cookie数据
cookies = response.cookies
print("响应的cookie数据:",cookies)
# 6.获取文本形式的响应内容
response_text = response.text
print("文本形式的响应内容:",response_text)
# 7.获取字节形式的响应内容
response_content = response.content
print("字节形式的响应内容",response_content)