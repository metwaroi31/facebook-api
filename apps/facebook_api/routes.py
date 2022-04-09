from flask import render_template, redirect, request, url_for, jsonify
import datetime
from apps.facebook_api import blueprint
from apps.facebook_api.utils import *
from apps.authentication.models import Users
from apps.facebook_api.forms import *
from flask_login import (
    current_user,
    login_user,
    logout_user
)
import json
from apps import db, login_manager
# @blueprint.route('/facebook/get_user', methods=['GET'])
# def getviplike_view():
#     result = getviplike('ngocdinh95')
#     return jsonify(result)

@blueprint.route('/facebook/add_like', methods=['GET', 'POST'])
def addlike_view():
    form = AddLikeForm(request.form)
    if request.method == 'GET':        
        return render_template('facebook/viplike.html', form=form)
    if request.method == 'POST':
        username = current_user.username
        user = Users.query.filter_by(username=username).first()

        facebook_id = request.form['facebook_id']
        name = request.form['name']
        time = request.form['time']
        like = request.form['like']
        
        total_coin_to_pay = int(time) * int(like) * 48
        if user.coin < total_coin_to_pay:
            return render_template('facebook/viplike.html', msg='you do not have enough coin, please buy more', form=form)
        
        result = json.loads(addlike(facebook_id, name, int(time), like, username + 'da su dung dich vu nay', 'coavt', 'LIKE'))
        print (result)
        # print (json.loads(result))
        if result['status'] == 'error':
            return render_template('facebook/viplike.html', msg=result['msg'], form=form)

        user.coin = user.coin - total_coin_to_pay
        db.session.commit()

        return render_template('facebook/viplike.html', msg='buy successfully', form=form)

@blueprint.route('/facebook/add_comment', methods=['GET', 'POST'])
def addcomment_view():
    form = AddCommentForm(request.form)
    if request.method == 'GET':        
        return render_template('facebook/vipcomment.html', form=form)
    if request.method == 'POST':
        username = current_user.username
        user = Users.query.filter_by(username=username).first()

        facebook_id = request.form['facebook_id']
        name = request.form['name']
        time = request.form['time']
        comments = request.form['comments']
        content = request.form['content']
        stop_command = request.form['stop_command']
        total_coin_to_pay = int(time) * int(comments) * 320
        if user.coin < total_coin_to_pay:
            return render_template('facebook/vipcomment.html', msg='you do not have enough coin, please buy more', form=form)
        
        result = json.loads(addcmt(facebook_id, name, int(time), comments, \
                                username + 'da su dung dich vu nay', content, stop_command))
        print (result)
        # print (json.loads(result))
        if result['status'] == 'error':
            return render_template('facebook/vipcomment.html', msg=result['msg'], form=form)

        user.coin = user.coin - total_coin_to_pay
        db.session.commit()

        return render_template('facebook/vipcomment.html', msg='buy successfully', form=add_comment_form)

@blueprint.route('/facebook/add_live', methods=['GET', 'POST'])
def addlive_view():
    form = AddMatForm(request.form)
    if request.method == 'GET':        
        return render_template('facebook/vipmat.html', form=form)
    if request.method == 'POST':
        username = current_user.username
        user = Users.query.filter_by(username=username).first()

        facebook_id = request.form['facebook_id']
        name = request.form['name']
        time = request.form['time']
        mat = request.form['mat']
    
        total_coin_to_pay = int(time) * int(mat) * 1200
        if user.coin < total_coin_to_pay:
            return render_template('facebook/vipmat.html', msg='you do not have enough coin, please buy more', form=form)
        
        result = json.loads(addlive(facebook_id, name, int(time), mat, \
                                username + 'da su dung dich vu nay'))
        print (result)
        # print (json.loads(result))
        if result['status'] == 'error':
            return render_template('facebook/vipmat.html', msg=result['msg'], form=form)

        user.coin = user.coin - total_coin_to_pay
        db.session.commit()

        return render_template('facebook/vipmat.html', msg='buy successfully', form=form)
