import codecs

from flask import Flask
# import markdown
# import codecs
from flask_cors import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/articles/<name>", methods=['GET', ])
def markdown(name):
    in_file = "C:\\Users\laomingming\PycharmProjects\\laomingmingBG\\posts\\" + str(name) + ".md"

    # name = argv[0]
    # in_file = '%s.md' % (name)

    # out_file = '%s.html' % (name)

    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()
    # html = markdown.markdown(text)
    html = markdown.markdown(text)
    return html

if __name__ == '__main__':
    CORS(app, supports_credentials=True) #解决跨域请求
    # app.debug = True
    app.run()
