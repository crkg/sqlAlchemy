from flask import Flask
from flask import make_response, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

class Someobject:
    @staticmethod
    def somemethod():
        return 5


#@app.route('/<path:name>')
def hello(name):
    return f'<h1> Hellow {name} </h1>'

app.add_url_rule(endpoint='hello',view_func=hello,rule='/<path:name>')

@app.route('/')
def index():
    response = make_response('<h1> This document is for index </h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/test/<name>')
def template_test(name):
    return render_template('hello.html',var_name=name, mydict={'ac':40}, mylist=[1,2,3,4], myindex=1, myObject=Someobject())

@app.route('/inherit/<name>')
def inherit_html(name):
    return render_template('inherit_hello.html',var_name=name, mydict={'ac':40}, mylist=[1,2,3,4], myindex=1, myObject=Someobject())

@app.route('/body/<name>')
def body(name):
    return render_template('bodytemplate.html',var_name=name)

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/user_name/<name>')
def user_info(name):
    return render_template('user_info.html',var_name=name)

if __name__ == '__main__':

    app.run(debug=True, port=5000)


