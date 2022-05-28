# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SelectField
from wtforms.validators import Email, DataRequired
from wtforms import validators
# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    phone = IntegerField('phone',
                      id='phone',
                      validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[
                                 DataRequired(),
                                 validators.EqualTo('password_confirm', message='Passwords must match')
                            ])
    password_confirm = PasswordField(label='Password confirm', validators=[
                            DataRequired(),
                            ])
