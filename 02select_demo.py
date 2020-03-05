import pymysql
# 建立连接
conn = pymysql.connect(host = 'localhost',user = 'root',password = 'root',database ='books',port =3306)
# 获取游标
cursor = conn.cursor()
# 执行:查询图书表数据,并打印
cursor.execute("select * from t_book;")
# 打印查询结果总记录数
print("总记录的条数为:",cursor.rowcount)
# 打印查询结果第一条数据
print("第一条数据:",cursor.fetchone())
# 获取查询全部结果,由于游标会自动下移.所以需重新执行查询语句再打印
cursor.execute("select * from t_book;")
# 打印全部结果
book_lists = cursor.fetchall()
print(book_lists)
# 遍历每一本书,并打印
for book in book_lists:
    print("书:",book[1])
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
