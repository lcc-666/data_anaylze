import pymysql


# sql语句作为参数传入
def getsql(sql):
    global result
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root", password="123456",
        database="data",
        charset="gbk")

    cursor = conn.cursor()
    if isinstance(sql, str):
        cursor.execute(sql)
        result = cursor.fetchall()
    if isinstance(sql, list):
        result = []
        for i in sql:
            cursor.execute(i)
            result.append(cursor.fetchall())

    cursor.close()

    conn.close()

    return result
