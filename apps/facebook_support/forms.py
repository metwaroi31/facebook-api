# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SelectField
from wtforms.validators import Email, DataRequired
from wtforms import validators
# login and registration


class FacebookIDUrl(FlaskForm):
    facebook_url = StringField('Facebook_url', id='facebook_url')
    # like_emotion = BooleanField()
    # haha_emotion = BooleanField()

class PostIDUrl(FlaskForm):
    post_url = StringField('Facebook_id', id='facebook_id')
    # subcategory_like = SelectField('', choices = [('like_v2', 'like_v2'), ('like_v6', 'like_v6')])