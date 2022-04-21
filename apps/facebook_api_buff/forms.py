# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SelectField
from wtforms.validators import Email, DataRequired
from wtforms import validators
# login and registration


class AddBuffLikeForm(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    subcategory_like = SelectField('Sub Category', choices = [('like_v2', 'like_v2'), ('like_v6', 'like_v6')])
    like = IntegerField()
    # like_emotion = BooleanField()
    # haha_emotion = BooleanField()

class AddBuffSubForm(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    # subcategory_like = SelectField('', choices = [('like_v2', 'like_v2'), ('like_v6', 'like_v6')])
    sub = IntegerField()