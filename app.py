from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print("访问主页成功！")
    return "success"

if __name__ == '__main__':
    app.run()