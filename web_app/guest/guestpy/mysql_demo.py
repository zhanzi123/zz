from pymysql import cursors,connect

# 连接数据库
conn = connect(host='127.0.0.1',
               user='root',
               password='123456',
               db='guest',
               charset='utf8mb4',
               cursorclass=cursors.DictCursor)
try:
    with conn.cursor() as cursor:
        # 创建嘉宾数据
        sql = 'insert into sign_guest (realname,phone,email,sign,event_id,create_time) values ("tom",18800110002,"tom@mail.com",0,1,Now());'
        cursor.execute(sql)
    conn.commit()

    with conn.cursor() as cursor:
        # 查询添加的嘉宾
        sql = 'select realname,phone,email,sign FROM sign_guest where phone=%s'
        cursor.execute(sql,('18800110002',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()