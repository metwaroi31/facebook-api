# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SelectField
from wtforms.validators import Email, DataRequired
from wtforms import validators

class PayMomoForm(FlaskForm):
    money = IntegerField()
    token = StringField()

class GetOTPForm(FlaskForm):
    phone_number = StringField('phone_number', id='phone_number')
    momo_password = StringField('momo_password', id='momo_password')    

class AddMomoForm(FlaskForm):
    phone_number = StringField('phone_number', id='phone_number')
    momo_password = StringField('momo_password', id='momo_password')
    momo_token = StringField('momo_token', id='momo_token')
