from flask import Flask, json, request
# from markdown import markdown
# import codecs
from flask_cors import *
import sqlite3
import uuid

app = Flask(__name__)
# url = '/home/ubuntu/usr/python/flask-Blackground-of-Vue/test.db'  #服务器路径
url = 'test.db'  # 本地路径


def sql_function(sql, val):
    conn = sqlite3.connect(url)
    cursor = conn.cursor()

    if val:
        cursor.execute(sql, val)
    else:
        cursor.execute(sql)
    data = cursor.fetchall()
    data = json.dumps(data)

    cursor.close()
    conn.commit()
    conn.close()
    return data


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['POST', ])
def login():
    data = request.data
    data = str(data, encoding='utf8')
    print(type(data))
    data = json.loads(data)
    print(data, type(data))

    account = data['account']
    password = data['password']

    conn = sqlite3.connect(url)

    # 创建一个Cursor:
    cursor = conn.cursor()
    sql = "SELECT * FROM user WHERE account=? AND password=?;"
    cursor.execute(sql, [account, password])
    db_data = cursor.fetchall()
    # json.dumps	将 Python 对象编码成 JSON 字符串
    # db_data = json.dumps(db_data)
    cursor.close()
    conn.commit()
    conn.close()
    # return "welcome"
    if db_data:
        print("success")
        return json.dumps(db_data)
    else:
        print("fail")
        return "fail"


@app.route('/get_user', methods=['POST', ])
def get_user():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)

    conn = sqlite3.connect(url)

    # 创建一个Cursor:
    cursor = conn.cursor()
    sql = "SELECT * FROM user WHERE Id=? ;"
    cursor.execute(sql, [data["UserId"]])
    data = cursor.fetchall()
    data = json.dumps(data)

    cursor.close()
    conn.commit()
    conn.close()
    return data


# 更新用户账户信息
@app.route('/update_user', methods=['POST', ])
def update_user():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)

    conn = sqlite3.connect(url)

    # 创建一个Cursor:
    cursor = conn.cursor()
    sql = "update user set Name = ?, Account=?, Password=? where ID=?;"
    cursor.execute(sql, [data["Name"], data["Account"], data["Password"], data["Id"]])
    data = cursor.fetchall()
    data = json.dumps(data)

    cursor.close()
    conn.commit()
    conn.close()
    return data


# 注册功能
@app.route("/register", methods=['POST', ])
def register():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)

    name = data['name']
    account = data['account']
    password = data['password']
    newId = str(uuid.uuid1())

    conn = sqlite3.connect(url)
    cursor = conn.cursor()
    sql = "insert into user (id,name,account, password) values (?,?,?,?);"
    cursor.execute(sql, [newId, name, account, password])
    row = cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()
    if row > 0:
        return newId
    else:
        return ""


# 检查账户名称是否已存在
@app.route("/check_username", methods=['POST', ])
def check_username():
    data = request.get_json()
    sql = "SELECT Account FROM user WHERE Account=? ;"
    val = [data['Account']]
    return sql_function(sql, val)


# 获取文章标题
@app.route("/title", methods=['GET', ])
def get_title():
    # 连接到SQLite数据库
    # 数据库文件是test.db

    # 如果文件不存在，会自动在当前目录创建:
    # conn = sqlite3.connect('/home/ubuntu/usr/python/flask-Blackground-of-Vue/test.db')
    # conn = sqlite3.connect('test.db')
    conn = sqlite3.connect(url)

    # 创建一个Cursor:
    cursor = conn.cursor()

    cursor.execute("SELECT id,title,createDate FROM articles;")
    # 返回多个元祖
    data = cursor.fetchall()
    # titles = str(titles)
    # json.dumps	将 Python 对象编码成 JSON 字符串
    # json.loads	将已编码的 JSON 字符串解码为 Python 对象
    data = json.dumps(data)
    # id = data[0][0:]
    # title = data[1][0:]
    # for i in data:
    #     data[i] = [id[i]+title[i]]

    # 关闭Cursor:
    cursor.close()

    # 提交事务:
    conn.commit()

    # 关闭Connection:
    conn.close()

    return data


# 获取编程类型文章的标题
@app.route("/code_title", methods=['GET', ])
def get_code_title():
    # 连接到SQLite数据库
    # 数据库文件是test.db

    # 如果文件不存在，会自动在当前目录创建:
    # conn = sqlite3.connect('/home/ubuntu/usr/python/flask-Blackground-of-Vue/test.db')
    # conn = sqlite3.connect('test.db')
    conn = sqlite3.connect(url)

    # 创建一个Cursor:
    cursor = conn.cursor()

    cursor.execute("SELECT id,title,createDate FROM articles WHERE type='code';")
    data = cursor.fetchall()
    data = json.dumps(data)

    # 关闭Cursor:
    cursor.close()

    # 提交事务:
    conn.commit()

    # 关闭Connection:
    conn.close()

    return data


# 获取文学类型文章的标题
@app.route("/lite_title", methods=['GET', ])
def get_lite_title():
    # 连接到SQLite数据库
    # 数据库文件是test.db

    # 如果文件不存在，会自动在当前目录创建:
    # conn = sqlite3.connect('/home/ubuntu/usr/python/flask-Blackground-of-Vue/test.db')
    # conn = sqlite3.connect('test.db')
    conn = sqlite3.connect(url)

    # 创建一个Cursor:
    cursor = conn.cursor()

    cursor.execute("SELECT id,title,createDate FROM articles WHERE type='lite';")
    data = cursor.fetchall()
    data = json.dumps(data)

    # 关闭Cursor:
    cursor.close()

    # 提交事务:
    conn.commit()

    # 关闭Connection:
    conn.close()

    return data


@app.route("/get_user_title", methods=['POST', ])
def get_user_title():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)

    conn = sqlite3.connect(url)

    # 创建一个Cursor:
    cursor = conn.cursor()

    cursor.execute("SELECT id,title,createDate FROM articles WHERE userId=?;", [data["UserId"]])
    data = cursor.fetchall()
    data = json.dumps(data)

    # 关闭Cursor:
    cursor.close()

    # 提交事务:
    conn.commit()

    # 关闭Connection:
    conn.close()

    return data


# 获取文章功能
@app.route("/get_article", methods=['POST', ])
def get_markdown():
    data = request.get_json()

    sql = "SELECT articles.ID, articles.userId,articles.title, articles.article,articles.createDate, articles.type, " \
          "user.Name " \
          "FROM articles as articles INNER JOIN user as user where articles.userId = user.Id and articles.ID=?;"
    val = [data["Id"]]

    return sql_function(sql, val)


# 插入文章功能
@app.route("/insert_article", methods=['POST', ])
def insert_article():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)

    newId = str(uuid.uuid1())

    conn = sqlite3.connect(url)
    cursor = conn.cursor()
    sql = "insert into articles (ID,userId,title,article,createDate,type) values (?,?,?,?,?,?);"
    cursor.execute(sql, [newId, data["userId"], data["title"], data["article"], data["createDate"], data["type"]])
    row = cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()
    if row > 0:
        return newId
    else:
        return ""


# 更新文章功能
@app.route("/update_article", methods=['POST', ])
def update_article():
    data = request.get_json()
    sql = "update articles set title = ?, article=?, createDate=?, type=? where ID=?;"
    val = [data["title"], data["article"], data["createDate"], data["type"], data["ID"]]
    return sql_function(sql, val)


# 删除文章功能
@app.route("/delete_article", methods=['POST', ])
def delete_article():
    data = request.get_json()
    sql = "DELETE from articles where Id = ?"
    val = [data["Id"]]
    return sql_function(sql, val)


# 增加Canvas功能
@app.route("/insert_canvas", methods=['POST', ])
def insert_canvas():
    data = request.get_json()
    newId = str(uuid.uuid1())
    sql = "insert into canvas (Id,UserId,Code,Date,Name) values (?,?,?,?,?);"
    val = [newId, data["UserId"], data["Code"], data["Date"], data["Name"]]
    return sql_function(sql, val)


# 删除Canvas功能
@app.route("/delete_canvas", methods=['POST', ])
def delete_canvas():
    data = request.get_json()
    sql = "DELETE from canvas where Id = ?"
    val = [data["Id"]]
    return sql_function(sql, val)


# 查找Canvas功能
@app.route("/select_canvas", methods=['POST', ])
def select_canvas():
    data = request.get_json()
    if "UserId" not in data:
        sql = "SELECT canvas.Id, canvas.UserId,canvas.Code, canvas.Date,canvas.Name, user.Name  " \
              "FROM canvas as canvas INNER JOIN user as user where canvas.UserId = user.Id;"
        val = []
    else:
        sql = "SELECT * FROM canvas where UserId=?;"
        val = [data["UserId"]]
    return sql_function(sql, val)


# 更新Canvas功能
@app.route("/update_canvas", methods=['POST', ])
def update_canvas():
    data = request.get_json()
    sql = "update canvas set Code = ?, Date=?, Name=? where Id=?;"
    val = [data["Code"], data["Date"], data["Name"], data["Id"]]
    return sql_function(sql, val)


# 获取图片功能
@app.route("/get_images", methods=['POST', ])
def get_image():
    data = request.get_json()
    if "UserId" not in data:
        sql = "SELECT Id, Name, LittleImage FROM images ;"
        val = []
    else:
        sql = "SELECT Id, Name, LittleImage FROM images where UserId=?;"
        val = [data["UserId"]]
    return sql_function(sql, val)


# 获取原图功能
@app.route("/get_one_image", methods=['POST', ])
def get_one_image():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)

    conn = sqlite3.connect(url)
    cursor = conn.cursor()

    cursor.execute("SELECT Image FROM images where Id=?;", [data["id"]])
    data = cursor.fetchall()
    data = json.dumps(data)

    cursor.close()
    conn.commit()
    conn.close()
    return data


# 添加图片功能
@app.route("/insert_image", methods=['POST', ])
def insert_image():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)

    newId = str(uuid.uuid1())

    conn = sqlite3.connect(url)
    cursor = conn.cursor()
    sql = "insert into images (Id,UserId, Name, LittleImage, Image, Date) values (?,?,?,?,?,?);"
    cursor.execute(sql, [newId, data["UserId"], data["Name"], data["LittleImage"], data["Image"], data["Date"]])
    row = cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()
    if row > 0:
        return newId
    else:
        return ""


# 删除图片功能
@app.route("/delete_image", methods=['POST', ])
def delete_image():
    data = request.get_json()
    sql = "DELETE from images where Id = ?"
    val = [data["Id"]]
    return sql_function(sql, val)


# 插入评论功能
@app.route("/insert_message", methods=['POST', ])
def insert_message():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)

    newId = str(uuid.uuid1())

    conn = sqlite3.connect(url)
    cursor = conn.cursor()
    sql = "insert into message (Id,ArticleId, UserName, Message, Date) values (?,?,?,?,?);"
    cursor.execute(sql, [newId, data["ArticleId"], data["UserName"], data["Message"], data["Date"]])
    row = cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()
    if row > 0:
        return newId
    else:
        return ""


# 删除评论功能
@app.route("/delete_message", methods=['POST', ])
def delete_message():
    data = request.get_json()
    sql = "DELETE from message where Id = ?;"
    val = [data["Id"]]
    return sql_function(sql, val)


# 获取评论功能
@app.route("/get_message", methods=['POST', ])
def get_message():
    data = request.get_json()
    sql = "SELECT * FROM message where ArticleId =? ;"
    val = [data["ArticleId"]]
    return sql_function(sql, val)


if __name__ == '__main__':
    CORS(app, supports_credentials=True)  # 解决跨域请求
    # app.debug = True
    # app.run(host='0.0.0.0', port=5000)
    app.run()
