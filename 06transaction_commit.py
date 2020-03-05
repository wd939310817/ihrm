import pymysql
# 建立连接
# (autocommit 写入语句(插入,更新,删除语句)都需要把自动提交事物的开关打开)
# 不提交事务,不会添加修改插入.只会在控制台看到
conn = pymysql.connect(host = 'localhost',user = 'root',password = 'root',
                       database ='books',port =3306)
# 获取游标
cursor = conn.cursor()
# 执行:增加图书
cursor.execute("insert into t_book(title,pub_date)values('龙族','1996-01-01');")
# 重新执行查询结果,才能打印查询结果
cursor.execute("select * from t_book;")
print("插入图书:",cursor.fetchall())
# 执行:增加作者
cursor.execute("insert into t_hero(`name`,gender,book_id)values('路明非','1',6)")
# 重新执行查询结果,才能打印查询结果
cursor.execute("select * from t_hero;")
# 打印结果
print("插入人物:",cursor.fetchall())
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
