import pymysql
# 建立连接
conn = pymysql.connect(host = 'localhost',user = 'root',password = 'root',
                       database ='books',port =3306,autocommit=False)
# 获取游标
cuosor = conn.cursor()
# 执行:查询版本
cuosor.execute('select version();')
# 获取执行结果
result =cuosor.fetchone()
# 打印执行结果
print('执行结果:',result)
# 关闭游标
cuosor.close()
# 关闭连接
conn.close()