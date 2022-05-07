# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import Email, DataRequired
from wtforms import validators
# login and registration


class AddLikeForm(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    name = StringField('name')
    time = IntegerField()
    like = IntegerField()
    like_emotion = BooleanField()
    haha_emotion = BooleanField()
    angry_emotion = BooleanField()
    heart_emotion = BooleanField()
    love_emotion = BooleanField()
    cry_emotion = BooleanField()
    wow_emotion = BooleanField()
    #  IntegerField(widget=NumberInput())

class UpdateLikeForm(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    like_emotion = BooleanField()
    haha_emotion = BooleanField()
    angry_emotion = BooleanField()
    heart_emotion = BooleanField()
    love_emotion = BooleanField()
    cry_emotion = BooleanField()
    wow_emotion = BooleanField()

class UpdateLikeFormExtend(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    like = IntegerField()
    time = IntegerField()

class AddCommentForm(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    name = StringField('name')
    time = IntegerField()
    comments = IntegerField()
    content = TextAreaField('content')
    image_url = StringField('image')
    stop_command = StringField('stop_command')

class UpdateCommentForm(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    content = StringField('content')
    image_url = StringField('image')
    stop_command = StringField('stop_command')

class UpdateCommentFormExtend(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    comments = IntegerField()
    time = IntegerField()

class AddMatForm(FlaskForm):
    facebook_id = StringField('Facebook_id', id='facebook_id')
    name = StringField('name')
    time = IntegerField()
    mat = IntegerField()

# class UpdateMatForm(FlaskForm):

# class AddMatForm(FlaskForm):
#     facebook_id = StringField('Facebook_id', id='facebook_id')
#     name = StringField('name')
#     time = IntegerField()
#     mat = IntegerField()

# class AddMatForm(FlaskForm):
#     facebook_id = StringField('Facebook_id', id='facebook_id')
#     name = StringField('name')
#     time = IntegerField()
#     mat = IntegerField()

# class AddMatForm(FlaskForm):
#     facebook_id = StringField('Facebook_id', id='facebook_id')
#     name = StringField('name')
#     time = IntegerField()
#     mat = IntegerField()

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
