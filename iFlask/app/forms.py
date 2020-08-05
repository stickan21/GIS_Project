# coding: utf-8

"""
    forms.py
    ~~~~~~~~
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import IntegerField, StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, EqualTo

class FeatureForm(FlaskForm):
    """ Feature Form"""
    member_id = StringField('Member')
    loan_amnt = StringField('Loan Amount')
    int_rate = StringField('Rate')
    installment = StringField('Installment')
    go = SubmitField('Submit')

class UploadForm(FlaskForm):
    DataFile = FileField('Your data file', validators=[
        FileRequired(),
        FileAllowed(['csv', 'txt'], 'plain text file only!')
    ])