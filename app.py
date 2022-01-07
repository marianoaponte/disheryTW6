from flask import Flask, render_template, flash, redirect
from complements.forms import *
from complements.config import Config

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')
app.config.from_object(Config)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html")

@app.route("/feed")
def feed():
    return render_template("feed.html")

@app.route("/login", methods=['GET', 'POST'])
def test():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.rememberme.data))
        return redirect('/index')

    return render_template("login.html", form=form)

@app.route("/register")
def test2():
    form = RegisterForm()
    return render_template("register.html", form=form)




if __name__ == '__main__':
    app.run()
