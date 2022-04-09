# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import Email, DataRequired
from wtforms import validators
# login and registration


class AddLikeForm(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    name = StringField('name')
    time = IntegerField()
    like = IntegerField()
    #  IntegerField(widget=NumberInput())

class AddCommentForm(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    name = StringField('name')
    time = IntegerField()
    comments = IntegerField()
    content = StringField('content')
    stop_command = StringField('stop_command')

class AddMatForm(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    name = StringField('name')
    time = IntegerField()
    mat = IntegerField()
    
# class 
# class CreateAccountForm(FlaskForm):
#     username = StringField('Username',
#                          id='username_create',
#                          validators=[DataRequired()])
#     email = StringField('Email',
#                       id='email_create',
#                       validators=[DataRequired(), Email()])
#     password = PasswordField('Password',
#                              id='pwd_create',
#                              validators=[
#                                  DataRequired(),
#                                  validators.EqualTo('password_confirm', message='Passwords must match')
#                             ])
#     password_confirm = PasswordField(label='Password confirm', validators=[
#                             DataRequired(),
#                             ])
