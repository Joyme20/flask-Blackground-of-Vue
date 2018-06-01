from flask import Flask, json
from markdown import markdown
import codecs
from flask_cors import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/title", methods=['GET', ])
def getTitle():
    import sqlite3
    # 连接到SQLite数据库
    # 数据库文件是test.db

    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('test.db')

    # 创建一个Cursor:
    cursor = conn.cursor()

    cursor.execute("SELECT id,title,createDate FROM articles;")
    data = cursor.fetchall()
    # titles = str(titles)
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


@app.route("/articles/<name>", methods=['GET', ])
def markdownToHtml(name):
    # in_file = "C:\\Users\laomingming\PycharmProjects\\laomingmingBG\\posts\\" + str(name) + ".md"
    # input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    # text = input_file.read()
    ## html = markdown.markdown(text)
    # html = markdown(text)
    # return html
    print(type(name))

    import sqlite3
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('test.db')

    # 创建一个Cursor:
    cursor = conn.cursor()

    #从数据库获取文章
    cursor.execute("SELECT article FROM articles where id=?;", (name))
    text = cursor.fetchone()

    #把从数据库获取的list格式的文章连接成字符串格式
    text = "".join(text)

    html = markdown(text)
    print(html)

    # 关闭Cursor:
    cursor.close()

    # 提交事务:
    conn.commit()

    # 关闭Connection:
    conn.close()



    return html

if __name__ == '__main__':
    CORS(app, supports_credentials=True) #解决跨域请求
    # app.debug = True
    app.run()
