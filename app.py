'''
flask项目一般默认将静态的配置文件放在static目录里, 将前端模板文件放在templates目录里
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

# 添加路由
@app.route("/hello")
def hello():
    return "hello world"

# 通过路由传参1
@app.route("/username/<username>")
def show_username(username):
    return f"user name is {username}"

# 通过路由传参并规定参数类型, 支持string，int，float，path，uuid
@app.route("/userid/<int:id>")
def show_userid(id):
    return f"user id is {id}"

# 渲染页面, 参数和对象, 只需输入被渲染的文件名，flask会自动从template目录里查找
# 参数page_id, user_name, user, my_dict会被传到index.html文件中
class User:
    def __init__(self, username, email) -> None:
        self.username = username
        self.email = email
my_dict = {"index":1, "feature":"good"}

@app.route("/index/<int:id>")
def main_page(id):
    user = User(username="python语言", email="123@python.com")
    return render_template("index.html", page_id=id, user_name="恭喜发财", user=user, my_dict=my_dict)

# 渲染css，javascript的效果
@app.route("/images")
def images():
    return render_template("image.html")

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

# 接收POST请求中的form表单
@app.route("/post_file", methods=["POST"])
def recieve_file():
    from PIL import Image 
    import numpy as np 

    id = request.form.get("id")
    image = request.files.get("images")
    image = Image.open(image)
    image = np.array(image)
    print(id, image)
    return_dict = {"id":id, "image":str(image)}
    return return_dict

if __name__ == '__main__':
    app.run()
