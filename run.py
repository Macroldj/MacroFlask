from datetime import datetime, timedelta

from flask import Flask, escape, url_for, request, render_template, Response
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def index():
    username = request.cookies.get('username','')
    print(username)
    return render_template('index.html', username=username)


@app.route('/logout')
def logout():
    response = redirect(url_for('login'))
    response.delete_cookie('username')
    return response


def show_login_form(error):
    return render_template("login.html",error = error)


def valid_login(username,password):
    if username == "lidejin" and password == "lidejin":
        return True
    else:
        return False


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form["username"], request.form["pass"]):
            res = Response('cookies的设置')
            expires = datetime.now() + timedelta(days=13, hours=16)
            res.set_cookie('username')
            print(res)
            return redirect(url_for('index'))
        else:
            error = '密码问题'
            return render_template("login.html", error = error)
    else:
        return render_template("login.html", error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug = True)