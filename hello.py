from flask import Flask
from flask import request

app = Flask(__name__)


#### ルーティング基礎 ####
@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

# ルーティング引数受け取り
@app.route("/test/<test>")
def test(test):
    return_test = "<p>test:{}</p>"
    return return_test.format(test)

# 引数型指定
@app.route("/test1/<int:test>")
def test1(test):
    return_test = "<p>test1:{}</p>"
    return return_test.format(test)

# @app.route() の代わりに app.add_url_rule() を使用
def test2():
    return "test2"
app.add_url_rule("/test2", view_func=test2)

#### データを受け取る ####

# requestオブジェクト
@app.route("/test3")
def test3():
    # メソッド・パス情報
    request_data = []
    request_data.append(request.method)
    request_data.append(request.url)
    request_data.append(request.host_url)
    request_data.append(request.scheme)
    request_data.append(request.host)
    request_data.append(request.path)
    # GETパラメータ
    request_data.append(request.args['key']) # ?key=hoge
    return request_data

# jsonデータ取得(POST)
@app.route("/test4", methods=["POST"])
def test4():
    request_body = request.get_json()
    return request_body