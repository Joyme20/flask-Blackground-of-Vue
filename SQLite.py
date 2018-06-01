# 导入SQLite驱动:
import codecs
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db

# 如果文件不存在，会自动在当前目录创建:
from flask import json
from markdown import markdown

conn = sqlite3.connect('test.db')

# 创建一个Cursor:
cursor = conn.cursor()

# 执行一条SQL语句，创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# <sqlite3.Cursor object at 0x10f8aa260>

# 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# <sqlite3.Cursor object at 0x10f8aa260>

# 通过rowcount获得插入的行数:
# cursor.rowcount
# 1
# in_file = "C:\\Users\laomingming\PycharmProjects\\laomingmingBG\\posts\\0.md"
# input_file = codecs.open(in_file, mode="rb", encoding="utf-8")
# text1 = input_file.read()
# text2 = "text2"
# createDate = "2018/05/30"

# print(text1)

# cursor.execute("INSERT INTO articles (title, data, createDate)"
#                "VALUES (?, ?, ?)",( 'title3', text1, createDate))
#
# #查看所有表名
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())
#
# cursor.execute("PRAGMA table_info({})".format("articles"))
# print(cursor.fetchall())

# cursor.execute("SELECT title FROM articles ;")
# print(cursor.fetchall())

cursor.execute("SELECT data FROM articles where id=?;",(str(6)))
text = cursor.fetchone()
# codecs.open(text, mode="r", encoding="utf-8")
# print(text)
# text = json.dumps(text)
# print(text)
# text = str(text)
text = "".join(text)
#去除首尾的中括号
# text = text[2:len(text)-2]
# print("去除首尾的中括号"+text+"aaa")
# print(len(text))

# text1 = text.replace("\n"," ")
# print("br"+text1)


# text1 = text1.split("\n")
print("br"+text)



#
# html = markdown(text)
# print("html"+html)



# 关闭Cursor:
cursor.close()

# 提交事务:
conn.commit()

# 关闭Connection:
conn.close()