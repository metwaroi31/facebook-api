from flask import render_template, redirect, request, url_for, jsonify
import datetime
from apps.facebook_api_buff import blueprint
from apps.facebook_api_buff.utils import *
from apps.authentication.models import Users
from apps.facebook_api_buff.forms import *
from flask_login import (
    current_user,
    login_user,
    logout_user
)
import json
from apps import db, login_manager
import ast

@blueprint.route('/facebook/buff_like', methods=['GET', 'POST'])
def bufflike_view():
    form = AddBuffLikeForm(request.form)
    # update_form = UpdateCommentForm(request.form)
    # update_form_extend = UpdateCommentFormExtend(request.form)
    # list_of_buff_like = getbufflike()
    # list_of_buff_like = list_of_buff_like['data']
    if request.method == 'GET':        
        return render_template('facebook/bufflike.html', form=form, render_template_string=parse_template,\
                                            parse_date=parse_date)
    if request.method == 'POST':
        print (request.form)
        username = current_user.username
        user = Users.query.filter_by(username=username).first()
        total_coin_to_pay = 0
        facebook_id = request.form['facebook_id']
        like_type = request.form['subcategory_like']
        like = request.form['like']
        if like_type == 'like_v2':
            total_coin_to_pay = int(like) * 32
        if like_type == 'like_v6':
            total_coin_to_pay = int(mat) * 64
        if user.coin < total_coin_to_pay:
            return render_template('facebook/bufflike.html', msg='you do not have enough coin, please buy more', form=form, \
                                        render_template_string=parse_template,\
                                            parse_date=parse_date)
        
        result = json.loads(addlive(facebook_id, name, int(time), mat, \
                                username + 'da su dung dich vu nay'))
        print (result)
        # print (json.loads(result))
        if result['status'] == 'error':
            return render_template('facebook/bufflike.html', form=form, render_template_string=parse_template,\
                                            parse_date=parse_date)

        user.coin = user.coin - total_coin_to_pay
        db.session.commit()

        return render_template('facebook/bufflike.html', form=form, render_template_string=parse_template,\
                                            parse_date=parse_date)
