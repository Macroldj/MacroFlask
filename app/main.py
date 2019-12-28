from flask import Flask, request, escape, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/index')
def xiao():
    return "xiaoli"


@app.route('/')
def hello_world():
    return "This is a aple"


@app.route("/app/<username>")
def name(username):
    return "my name is {}".format(escape(username))


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return "post funciton"
    else:
        return "post "


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))


@app.route('/login2/<username>')
def loginFunction(username):
     return render_template('index.html', username=username)


app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)