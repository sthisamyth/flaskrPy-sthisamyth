#!/usr/bin/python
# encoding: utf-8

import MySQLdb
import mysql_config

# 返回字典（目前没用上）
def Fetchall(sql):
# 打开数据库连接
    try:
         db = MySQLdb.Connection(host=mysql_config.DB_HOST, user=mysql_config.DB_USER, passwd=mysql_config.DB_PASSWORD, db=mysql_config.DB_DATABASE, charset='utf8')
# 使用cursor()方法获取操作游标
         cur = db.cursor(MySQLdb.cursors.DictCursor)
# 使用execute方法执行SQL语句
         cur.execute(sql)
# 使用 fetchALL() 方法获取所有数据。
         data = cur.fetchall()
         return data
    except MySQLdb.Error, e:
        print "Mysqldb Error:%s" % e
# 关闭数据库连接
    finally:

        cur.close()
        db.close()

# 返回一个
def Fetchone(sql):
# 打开数据库连接
    try:
         db = MySQLdb.Connection(host=mysql_config.DB_HOST, user=mysql_config.DB_USER, passwd=mysql_config.DB_PASSWORD, db=mysql_config.DB_DATABASE, charset='utf8')
# 使用cursor()方法获取操作游标
         cur = db.cursor(MySQLdb.cursors.DictCursor)
# 使用execute方法执行SQL语句
         cur.execute(sql)
# 使用 fetchALL() 方法获取所有数据。
         data = cur.fetchone()
         return data
    except MySQLdb.Error, e:
        print "Mysqldb Error:%s" % e
# 关闭数据库连接
    finally:

        cur.close()
        db.close()

# 返回数组
def Fetchallsz(sql):
# 打开数据库连接
    try:
         db = MySQLdb.Connection(host=mysql_config.DB_HOST, user=mysql_config.DB_USER, passwd=mysql_config.DB_PASSWORD, db=mysql_config.DB_DATABASE, charset='utf8')
# 使用cursor()方法获取操作游标
         cur = db.cursor()
# 使用execute方法执行SQL语句
         cur.execute(sql)
# 使用 fetchALL() 方法获取所有数据。
         data = cur.fetchall()
         return data
    except MySQLdb.Error, e:
        print "Mysqldb Error:%s" % e
# 关闭数据库连接
    finally:

        cur.close()
        db.close()