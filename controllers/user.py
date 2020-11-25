from datetime import datetime, timedelta

from flask import render_template, request, url_for, make_response
from werkzeug.utils import redirect

from controllers import users


@users.route('/index')
def index():
    username = request.cookies.get('username','')
    if username:
        return render_template('index.html', username=username)
    else:
        return render_template('index.html', username=None)


@users.route('/logout')
def logout():
    response = redirect(url_for('users.index'))
    response.delete_cookie('username')
    return response


def show_login_form(error):
    return render_template("login.html",error = error)


def valid_login(username,password):
    if username == "lidejin" and password == "lidejin":
        return True
    else:
        return False


@users.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form["username"], request.form["pass"]):
            resp = make_response(render_template('index.html', username = request.form["username"]))
            expires = datetime.now() + timedelta(days=13, hours=16)
            resp.set_cookie('username',request.form['username'],expires=expires)
            return resp
        else:
            error = '密码问题'
            return render_template("login.html", error = error)
    else:
        return render_template("login.html", error=error)