from flask import Flask, render_template, flash, redirect, jsonify, request, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from complements.forms import *
from complements.config import Config
from complements import db
from werkzeug.security import generate_password_hash, check_password_hash
from complements.models import User, Recipe
from bson.json_util import dumps

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')
app.config.from_object(Config)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/feed", methods=['GET', 'POST'])
def feed():
    form = SearchForm()
    button_form = ''
    rec_data = list()

    if form.validate_on_submit():
        query1 = {"recipename": form.search_string.data}
        searched_data = db.recipes_col.find(query1)

        for recipe in searched_data:
            rec_data.append(recipe)

        print(rec_data)

    if request.method == 'POST':
        if request.form.get('val'):
            return redirect(url_for('reciperoute', recipe=request.form.get('val')))

    return render_template("feed.html", form=form, rec_data=rec_data)


@app.route("/recipe/<recipe>")
def reciperoute(recipe):
    query1 = {"recipename": recipe}
    recipe = db.recipes_col.find_one(query1)

    inglist = recipe['ingredients']
    qtlist = recipe['quantity']
    mslist = recipe['measure']

    return render_template("recipe.html", recipe=recipe, inglist=inglist, qtlist=qtlist, mslist=mslist)


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


entryno = 0


@app.route("/recipeingno", methods=['GET', 'POST'])
@login_required
def recipeingno():
    form = EntryForm()

    if form.validate_on_submit():
        global entryno
        entryno = form.entrynumber.data
        flash("{}".format(entryno))
        return redirect("/newrecipe")

    return render_template("recipeingno.html", form=form)


@app.route("/newrecipe", methods=['GET', 'POST'])
@login_required
def newrecipe():
    class LocalForm(AddRecipeForm): pass

    LocalForm.ingredients = FieldList(FormField(IngredientEntry), min_entries=entryno, validators=[DataRequired()])

    form = LocalForm()
    if form.validate_on_submit():
        inglist = []
        qtlist = []
        mslist = []

        for field in form.ingredients:
            inglist.append(field.ingredient.data)
            qtlist.append(field.quantity.data)
            mslist.append(field.measure.data)

        to_add = Recipe(recipename=form.recipename.data, base=form.base.data, ingredients=inglist, quantity=qtlist, measure=mslist)

        db.recipes_col.insert_one(to_add.__dict__)

        flash("{}".format(to_add))

        return redirect("/feed")

    return render_template("newrecipe.html", form=form)


if __name__ == '__main__':
    app.run()

login = LoginManager(app)


@login.user_loader
def load_user(id):
    userdict = db.users_col.find_one({"username": id})
    user = User(userdict['username'])
    user.set_pwhash(self=user, password=userdict['password_hash'])
    return user
