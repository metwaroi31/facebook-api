from flask import render_template, redirect, request, url_for, jsonify
import datetime
from apps.facebook_support import blueprint
from apps.facebook_support.utils import *
from apps.authentication.models import Users
from apps.facebook_support.forms import *
from flask_login import (
    current_user,
    login_user,
    logout_user
)
import json
from apps import db, login_manager
import ast

@blueprint.route('/facebook/support_get_facebook', methods=['GET', 'POST'])
def get_id_profile_view():
    form = FacebookIDUrl(request.form)
    # update_form = UpdateCommentForm(request.form)
    # update_form_extend = UpdateCommentFormExtend(request.form)
    # list_of_buff_like = getbufflike()
    # list_of_buff_like = list_of_buff_like['data']
    if request.method == 'GET':        
        return render_template('facebook/getid_profile.html', form=form)
    if request.method == 'POST':
        facebook_id = request.form['facebook_url']
        facebook_id = get_facebook_id(facebook_id)
        return render_template('facebook/getid_profile.html', msg=facebook_id, form=form)

@blueprint.route('/facebook/support_get_post', methods=['GET', 'POST'])
def get_id_post_view():
    form = PostIDUrl(request.form)
    if request.method == 'GET':        
        return render_template('facebook/getid_post.html', form=form)
    if request.method == 'POST':
        facebook_id = request.form['post_url']
        facebook_id = get_facebook_post_id(facebook_id)

        return render_template('facebook/getid_post.html', msg=facebook_id, form=form)
