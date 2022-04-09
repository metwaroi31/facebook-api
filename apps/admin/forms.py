# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import Email, DataRequired
from wtforms import validators
# login and registration


class UserForm(FlaskForm):
    coin = IntegerField()
    