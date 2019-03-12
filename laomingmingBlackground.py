from flask import Flask, json, request
# from markdown import markdown
# import codecs
from flask_cors import *
import sqlite3
import uuid

app = Flask(__name__)
# url = '/home/ubuntu/usr/python/flask-Blackground-of-Vue/test.db'  #服务器路径
url = 'test.db'  # 本地路径


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['POST', ])
def login():
    # account = request.form.get('account')
    # password = request.form.get('password')
    # print ("req",request.form)
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


@app.route("/articles/<article_id>", methods=['GET', ])
def get_markdown(article_id):
    # in_file = "C:\\Users\laomingming\PycharmProjects\\laomingmingBG\\posts\\" + str(name) + ".md"
    # input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    # text = input_file.read()
    # html = markdown.markdown(text)
    # html = markdown(text)
    # return html
    print(type(id))

    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    # conn = sqlite3.connect('/home/ubuntu/usr/python/flask-Blackground-of-Vue/test.db')
    # conn = sqlite3.connect('test.db')
    conn = sqlite3.connect(url)

    # 创建一个Cursor:
    cursor = conn.cursor()

    # 从数据库获取文章
    cursor.execute("SELECT article FROM articles where ID=?;", [article_id])
    text = cursor.fetchone()

    # 把从数据库获取的list格式的文章连接成字符串格式
    text = "".join(text)

    # html = markdown(text)
    # print(text)

    # 关闭Cursor:
    cursor.close()

    # 提交事务:
    conn.commit()

    # 关闭Connection:
    conn.close()
    return text


@app.route("/insert_article", methods=['POST', ])
def insert_article():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)
    # data = [title,article,createDate,type]
    # name = data['name']
    # account = data['account']
    # password = data['password']
    newId = str(uuid.uuid1())

    conn = sqlite3.connect(url)
    cursor = conn.cursor()
    sql = "insert into articles (id,userId,title,article,createDate,type) values (?,?,?,?,?,?);"
    cursor.execute(sql, [newId, data["userId"], data["title"], data["article"], data["createDate"], data["type"]])
    row = cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()
    if row > 0:
        return newId
    else:
        return ""


@app.route("delete_article",methods=['POST',])
def delete_article():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)


@app.route("/get_images", methods=['GET', ])
def get_image():
    conn = sqlite3.connect(url)
    cursor = conn.cursor()

    cursor.execute("SELECT Id, Name, LittleImage FROM images ;")
    data = cursor.fetchall()
    data = json.dumps(data)

    cursor.close()
    conn.commit()
    conn.close()
    return data


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


@app.route("/insert_image", methods=['POST', ])
def insert_image():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)

    newId = str(uuid.uuid1())

    conn = sqlite3.connect(url)
    cursor = conn.cursor()
    sql = "insert into images (Id,UserId, Name, LittleImage, Image) values (?,?,?,?,?);"
    cursor.execute(sql, [newId, data["UserId"], data["Name"], data["LittleImage"], data["Image"]])
    row = cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()
    if row > 0:
        return newId
    else:
        return ""
    # return data


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


@app.route("/get_message", methods=['POST', ])
def get_message():
    data = request.data
    data = str(data, encoding='utf8')
    data = json.loads(data)
    conn = sqlite3.connect(url)
    cursor = conn.cursor()

    # if(type())
    cursor.execute("SELECT * FROM message where ArticleId =? ;", data["ArticleId"])
    data = cursor.fetchall()
    data = json.dumps(data)

    cursor.close()
    conn.commit()
    conn.close()
    return data


if __name__ == '__main__':
    CORS(app, supports_credentials=True)  # 解决跨域请求
    # app.debug = True
    # app.run(host='0.0.0.0', port=5000)
    app.run()
