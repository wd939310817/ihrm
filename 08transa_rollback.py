#  回滚事务  (回到以前)
# (autocommit的真假为事务的状态 写入语句(插入,更新,删除语句)都需要把自动提交事物的开关打开)
    # 不提交事务,不会添加修改插入.只会在控制台看到 conn.rollback()为手动打开
import pymysql
conn,cursor=None,None
try:
    # 建立连接

    conn = pymysql.connect(host = 'localhost',user = 'root',password = 'root',
                           database ='books',port =3306)
    # 获取游标
    cursor = conn.cursor()
    # 执行:增加图书
    cursor.execute("insert into t_book(title,pub_date)values('龙族LV','1996-01-01');")
    # 重新执行查询结果,才能打印查询结果
    cursor.execute("select * from t_book;")
    print("插入图书:",cursor.fetchall())
    # 执行:增加作者
    # cursor.execute("insert into t_hero(`name`,gender,book_id)values('路明泽','1',6)")
    # 插入失败的语句 , 不执行,调到回滚事务
    cursor.execute("insert into t_hero(`name`,gender,book_id)values('路明泽','1')")
    # 重新执行查询结果,才能打印查询结果
    cursor.execute("select * from t_hero;")
    # 打印结果
    print("插入人物:",cursor.fetchall())
    # 手动提交事务
    conn.commit()
except Exception as e:
    if conn:
        # 手动回滚事务
        conn.rollback()
    if cursor:
        # 查询回滚后的当前事务(书和人)是否存在
        cursor.execute("select * from t_book;")
        print("回滚后,插入的图书:",cursor.fetchall())
        cursor.execute("select * from t_hero;")
        print("回滚后,插入的人物:",cursor.fetchall())
finally:
    if conn:
        # 关闭游标
        cursor.close()
    if cursor:
        # 关闭连接
        conn.close()
