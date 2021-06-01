# flask_wtf ext uses python classes to represent forms
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

# class Todo inherits from FlaskForm
class Todo(FlaskForm): 
    content = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Submit todo')