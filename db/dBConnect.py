# -*- coding: utf-8 -*-
# @Time       : 2019/12/13 15:22
# @Author     : SMnRa
# @Email      : smnra@163.com
# @File       : dBConnect.py
# @Software   : PyCharm
# @description: 本脚本的作用为 创建数据库连接



import cx_Oracle as oracle
import psycopg2 as postgres

try:
    import dbConfig as dbConfig
except ModuleNotFoundError :
    import db.dbConfig as dbConfig


def connDb(dbType):
    # 连接配置文件指定的数据库,返回 conn 和 curs
    # dbType 的 值为'oracle' 或 'postgres'
    # 根据传入的数据库类型名称返回相应的数据库连接对象
    try:
        if dbType=='oracle':
            conn = oracle.connect('{}/{}@{}:{}/{}'.
                format(dbConfig.oracleServer['user'],
                       dbConfig.oracleServer['password'],
                       dbConfig.oracleServer['ip'],
                       dbConfig.oracleServer['port'],
                       dbConfig.oracleServer['servername'] ))

            curs = conn.cursor()
            return conn,curs

        elif  dbType=='postgres':
            conn = postgres.connect(
                database=dbConfig.postgresServer['dbname'],
                user=dbConfig.postgresServer['user'],
                password=dbConfig.postgresServer['password'],
                host=dbConfig.postgresServer['host'],
                port=dbConfig.postgresServer['port'] )
            curs = conn.cursor()
            return conn,curs

    except Exception as e:
        print(e)
        return False, False

def changeDb(cursor,sql):
    try:
        cursor.execute(sql)
        cursor.execute("commit")
        return 1
    except Exception as e:
        print(e)
        return 0


def close(conn,curs):
    curs.execute("commit")
    curs.close()
    conn.close()


if __name__=='__main__':
    conn, curs = connDb('postgres')
    changeDb(curs, 'select *  from c_lte_custom')
    close(conn,curs)