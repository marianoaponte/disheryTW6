from flask import Flask, render_template, flash, redirect, jsonify
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from complements.forms import *
from complements.config import Config
from complements import db
from werkzeug.security import generate_password_hash, check_password_hash
from complements.models import User

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')
app.config.from_object(Config)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addrecipe")
@login_required
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
    if current_user.is_authenticated:
        return redirect("/feed")

    form = LoginForm()
    if form.validate_on_submit():
        userdict = db.users_col.find_one({"username": form.username.data})

        if userdict is None:
            flash("Invalid username!")
            return redirect("/login")

        user = User(userdict['username'])
        user.set_pwhash(self=user, password=userdict['password_hash'])

        if not User.check_password(user, form.password.data):
            flash("Invalid password.")
            return redirect("/login")

        login_user(user, remember=form.rememberme.data)
        return redirect("/feed")

    return render_template("login.html", form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect("/feed")

    form = RegisterForm()

    if form.validate_on_submit():
        form = RegisterForm()
        if form.validate_on_submit():
            user = User(username=form.username.data)
            user.set_password(self=user, password=form.password.data)
            db.users_col.insert_one(user.__dict__)
            flash('Registration of user {} completed successfully. Login now, please.'.format(form.username.data))
            return redirect("/login")

    return render_template("register.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    app.run()


login = LoginManager(app)


@login.user_loader
def load_user(id):
    userdict = db.users_col.find_one({"username": id})
    user = User(userdict['username'])
    user.set_pwhash(self=user, password=userdict['password_hash'])
    return user
