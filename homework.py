import pymysql
# 建立连接
conn = pymysql.connect(host = 'localhost',user = 'root',password = 'root',
                       database ='books',port =3306)
# 获取游标
cursor = conn.cursor()
# 1.插入一本书，书名为‘python从入门到放弃’，阅读量为50，评论量为0，发布日志为：2020-01-01
cursor.execute("insert into t_book(id,title,pub_date,`read`,comment)values(4,'python从入门到放弃','2020-01-01', 50,0);")
# 重新执行查询结果,才能打印查询结果
cursor.execute("select * from t_book;")
print('增加的图书:',cursor.fetchall())

# 2.测试工程师人员发现一个bug，这个本书的评论数与实际不符，要求你把评论量修改为修正后的值：250
cursor.execute("update t_book set `read`=250 where title='python从入门到放弃';")
cursor.execute("select * from t_book;")
print('修改后的评论:',cursor.fetchall())

# 3.- 老板投资了python，觉得这本书名太不吉利，需要下架，请删除这本书。
cursor.execute("delete from t_book  where title='python从入门到放弃';")
cursor.execute("select * from t_book;")
print('删除后的:',cursor.fetchall())

# 4.- 你删除后，心中不放心到底有没有删除，想确认是否真正删除了，你需要怎么做？
cursor.execute("select * from t_book;")
title='python从入门到放弃'
if title==True:
    print("书:",cursor.fetchall())
else:
    print(" 没有查询到'python从入门到放弃'这本书 ")
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
