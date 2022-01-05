from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FieldList
from wtforms.validators import DataRequired


#LOGIN FORM
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberme = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


#REGISTER FORM
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


#ADD RECIPE FORM
class AddRecipeForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    base = IntegerField('Base')
    ingredients = FieldList(StringField('Ingredient', validators=[DataRequired()]))
    quantity = FieldList(StringField('Ingredient', validators=[DataRequired()]))
    measure = FieldList(StringField('Ingredient', validators=[DataRequired()]))
    #to add: photo field


#REVIEW FORM
class ReviewForm(FlaskForm):
    rating = IntegerField('Rating')


#SEARCH FORM
class SearchForm(FlaskForm):
    search_string = StringField('Search', validators=[DataRequired()])
