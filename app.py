'''
flask项目一般默认将静态的配置文件放在static目录里，将前端模板文件放在templates目录里
'''

from flask import Flask, redirect, url_for, render_template, request

from static import config 

# 实例化Flask类，得到app对象
app = Flask(__name__)

# 加载配置文件
app.config.from_object(config)

# 主页
@app.route("/")
def index():
    return "Index Page"

# 渲染页面, 只需输入被渲染的文件名，flask会自动从template目录里查找
@app.route("/index")
def main_route():
    return render_template("index.html")

# 添加路由
@app.route("/hello")
def hello():
    return "hello world"

# 通过路由传参1
@app.route("/username/<username>")
def show_username(username):
    return f"user name is {username}"

# 通过路由传参并规定参数类型
@app.route("/userid/<int:id>")
def show_userid(id):
    return f"user id is {id}"

# 通过关键字参数传参
# book/list?page=100
@app.route("/book/list")
def book_list():
    page = request.args.get("page", default=1, type=int)
    return f"您查询的是第{page}个图书列表！"


# 指定请求类型
@app.route("/login", methods=["POST", "GET"])
def login():
    error = None 
    if request.method == "POST":
        return "post request!"
    elif request.method == "GET":
        return "get request!"
    else:
        raise Exception("do not support this request method!")

 

if __name__ == '__main__':
    app.run()
