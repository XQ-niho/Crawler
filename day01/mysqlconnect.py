# coding=utf-8

import pymysql

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '123',
                             database = 'test',
                             charset = 'utf8')

try:
    with connection.cursor() as cursor:
        sql = 'select * from student'
        cursor.execute(sql)

        result_set = cursor.fetchall()

        for row in result_set:
            print(row)
finally:
    connection.close()

