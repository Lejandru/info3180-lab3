from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    userName = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
