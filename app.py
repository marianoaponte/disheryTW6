from flask import Flask, render_template, flash, redirect, jsonify
from flask_login import LoginManager
from complements.forms import *
from complements.config import Config
from complements import db
from werkzeug.security import generate_password_hash, check_password_hash
from complements import models

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')
app.config.from_object(Config)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html")


@app.route("/feed", methods=['GET', 'POST'])
def feed():
    form = SearchForm()

    if form.validate_on_submit():
        flash('Searched {} recipe'.format(form.search_string.data))

    return render_template("feed.html", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        userdata = db.users_col.find_one({"username": form.username.data})
        if userdata is not None:
            if check_password_hash(userdata['password'], form.password.data) or form.password.data is None:
                return redirect("/feed")
            else:
                flash("Password was not correct.")
        else:
            flash("User does not exists.")

    return render_template("login.html", form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # if user exists, then error
        if db.users_col.find_one({"username": form.username.data}):
            flash("Username already in use.".format(form.username.data))

        else:
            post = {"username": form.username.data, "password": generate_password_hash(form.password.data)}
            db.users_col.insert_one(post)

            flash('Registration of user {} completed successfully. Login now, please.'.format(form.username.data))
            return redirect("/login")

    return render_template("register.html", form=form)


if __name__ == '__main__':
    app.run()

"""
login = LoginManager(app)
"""
