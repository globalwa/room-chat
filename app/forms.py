from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class IndexForm(FlaskForm):
    name = StringField('', validators=[DataRequired(message='Please, enter your name!')])
    room = StringField('', validators=[DataRequired(message='Please, enter your room!')])
    submit = SubmitField('Go on')