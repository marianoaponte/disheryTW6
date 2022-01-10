from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FieldList, FormField, FileField
from wtforms.validators import DataRequired, Length, EqualTo


# LOGIN FORM
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberme = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# REGISTER FORM
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=16)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


# ENTRY FORM
class EntryForm(FlaskForm):
    entrynumber = IntegerField('No of ingredients', validators=[DataRequired()])
    submit = SubmitField("Let's get started!")


# INGREDIENT ENTRY FORM
class IngredientEntry(FlaskForm):
    ingredient = StringField('Ingredient', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    measure = StringField('Measure Unit', validators=[DataRequired()])


# ADD RECIPE FORM
class AddRecipeForm(FlaskForm):
    """
    entryno = 0

    def __init__(self, entries, **kwargs):
        super().__init__(**kwargs)
        self.entryno = entries
    """

    recipename = StringField('Recipe Name', validators=[DataRequired()])
    base = IntegerField('Base')
    ingredients = FieldList(FormField(IngredientEntry), min_entries=0, validators=[DataRequired()])
    # pic = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Submit Recipe')


# REVIEW FORM
class ReviewForm(FlaskForm):
    rating = IntegerField('Rating')
    submit = SubmitField('Submit Review')


# SEARCH FORM
class SearchForm(FlaskForm):
    search_string = StringField('Search')
    submit = SubmitField('Go')


# TEST FORM ENTRY
class TestFormEntry(FlaskForm):
    field = StringField('Field')
    field2 = StringField('Field2')
    field3 = StringField('Field3')


# TEST FORM
class TestForm(FlaskForm):
    list = FieldList(FormField(TestFormEntry), min_entries=3)
    # gennaro = StringField("Gennaro")
    submit = SubmitField('Go')
