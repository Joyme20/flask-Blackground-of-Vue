import sqlite3
import uuid


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
    print(type(id))

    conn = sqlite3.connect(url)

    # 创建一个Cursor:
    cursor = conn.cursor()

    # 从数据库获取文章
    cursor.execute("SELECT * FROM articles where ID=?;", [article_id])

    # text = cursor.fetchone()
    # # 把从数据库获取的list格式的文章连接成字符串格式
    # text = "".join(text)

    data = cursor.fetchall()
    data = json.dumps(data)

    # html = markdown(text)
    # print(text)

    # 关闭Cursor:
    cursor.close()

    # 提交事务:
    conn.commit()

    # 关闭Connection:
    conn.close()
    return data


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


@app.route("/update_article", methods=['POST', ])
def update_article():
    data = request.get_json()
    sql = "update articles set title = ?, article=?, createDate=?, type=? where ID=?;"
    val = [data["title"], data["article"], data["createDate"], data["type"], data["ID"]]
    return sql_function(sql, val)


@app.route("/delete_article", methods=['POST', ])
def delete_article():
    data = request.get_json()
    sql = "DELETE from articles where Id = ?"
    val = [data["Id"]]
    return sql_function(sql, val)