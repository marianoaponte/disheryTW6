from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FieldList
from wtforms.validators import DataRequired, Length, EqualTo


#LOGIN FORM
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberme = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


#REGISTER FORM
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=16)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


#ADD RECIPE FORM
class AddRecipeForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    base = IntegerField('Base')
    ingredients = FieldList(StringField('Ingredient', validators=[DataRequired()]))
    quantity = FieldList(StringField('Quantity', validators=[DataRequired()]))
    measure = FieldList(StringField('Measure Unit', validators=[DataRequired()]))
    #to add: photo field
    submit = SubmitField('Submit Recipe')


#REVIEW FORM
class ReviewForm(FlaskForm):
    rating = IntegerField('Rating')
    submit = SubmitField('Submit Review')


#SEARCH FORM
class SearchForm(FlaskForm):
    search_string = StringField('Search')
    submit = SubmitField('Search Recipe')
