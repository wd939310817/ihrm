import pymysql
# 建立连接(autocommit 写入语句(插入,更新,删除语句)都需要把自动提交事物的开关打开)
conn = pymysql.connect(host = 'localhost',user = 'root',password = 'root',
                       database ='books',port =3306,autocommit=True)
# 获取游标
cursor = conn.cursor()
# 执行:(修改)阅读量+1,并打印
cursor.execute("update t_book set `read`=`read`+1 where title='三体';")
# 重新执行查询结果,才能打印查询结果
cursor.execute("select * from t_book;")
# 打印全部结果
book_lists = cursor.fetchall()
print(book_lists)
# 遍历每一本书,并打印
for book in book_lists:
    print("书:",book)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
