from flask import render_template, redirect, request, url_for, jsonify
import datetime
from apps.facebook_api_vip import blueprint
from apps.facebook_api_vip.utils import *
from apps.authentication.models import Users
from apps.facebook_api_vip.forms import *
from flask_login import (
    current_user,
    login_required
)
import json
from apps import db, login_manager
import ast
# @blueprint.route('/facebook/get_user', methods=['GET'])
# def getviplike_view():
#     result = getviplike('ngocdinh95')
#     return jsonify(result)

@blueprint.route('/add_like', methods=['GET', 'POST'])
@login_required
def addlike_view():
    # declare necessary variables for template
    form = AddLikeForm(request.form)
    update_form = UpdateLikeForm(request.form)
    update_form_extend = UpdateLikeFormExtend(request.form)
    list_of_vip_like = ast.literal_eval(getviplike('ngocdinh95'))
    list_of_vip_like = list_of_vip_like['data']
    list_of_vip_like = filter_list(list_of_vip_like, current_user.username)
    # print (list_of_vip_like)
    if request.method == 'GET':        
        return render_template('facebook/viplike.html', form=form, viplike=list_of_vip_like, \
                                               update_form=update_form, render_template_string=parse_template,\
                                                parse_date=parse_date, update_form_extend=update_form_extend, user=current_user)

    if request.method == 'POST':
        # update vip like
        if 'updatelike' in request.form:
            facebook_id = request.form['facebook_id']
            emotion_input = parse_emotion(request.form)
            result = json.loads(updateLike(facebook_id, emotion_input))
            return render_template('facebook/viplike.html', msg=result['msg'], form=form, viplike=list_of_vip_like, \
                                               update_form=update_form, render_template_string=parse_template, \
                                                parse_date=parse_date, update_form_extend=update_form_extend, user=current_user)
        # extend vip like
        if 'updatelikeextend' in request.form:
            username = current_user.username
            facebook_id = request.form['facebook_id']
            time = request.form['time']
            like = request.form['like']
            total_coin_to_pay = int(time) * int(like) * 48
            result = json.loads(giahanlike(facebook_id, time))
            user = Users.query.filter_by(username=username).first()
            user.coin = user.coin - total_coin_to_pay
            db.session.commit()
            return render_template('facebook/viplike.html', msg=result['msg'], form=form, viplike=list_of_vip_like, \
                                               update_form=update_form, render_template_string=parse_template, \
                                                parse_date=parse_date, update_form_extend=update_form_extend, user=current_user)
        # buy vip like
        username = current_user.username
        user = Users.query.filter_by(username=username).first()
        # Getting input from 
        emotion_input = ''
        facebook_id = request.form['facebook_id']
        name = request.form['name'] + "_" + username
        time = request.form['time']
        like = request.form['like']
        emotion_input = parse_emotion(request.form)
        # Coins calculating
        total_coin_to_pay = int(time) * int(like) * 48
        if user.coin < total_coin_to_pay:
            return render_template('facebook/viplike.html', msg='you do not have enough coin, please buy more', \
                            render_template_string=parse_template, form=form,\
                                update_form=update_form, viplike=list_of_vip_like, \
                                    parse_date=parse_date, update_form_extend=update_form_extend)
        result = json.loads(addlike(facebook_id, name, int(time), like,\
                                     username + 'da su dung dich vu nay', 'noavt', emotion_input))
        if result['status'] == 'error':
            return render_template('facebook/viplike.html', msg=result['msg'], form=form,\
                            render_template_string=parse_template, \
                                update_form=update_form, viplike=list_of_vip_like, \
                                    parse_date=parse_date, update_form_extend=update_form_extend)
        user.coin = user.coin - total_coin_to_pay
        db.session.commit()
        return render_template('facebook/viplike.html', msg='buy successfully',\
                            render_template_string=parse_template, \
                                update_form=update_form, form=form, viplike=list_of_vip_like,\
                                    parse_date=parse_date, update_form_extend=update_form_extend)

@blueprint.route('/facebook/add_like/<facebook_id>')
@login_required
def dellike_view(facebook_id):
    result = json.loads(dellike(facebook_id))
    return redirect(url_for('facebook_api_vip_blueprint.addlike_view'))

@blueprint.route('/add_comment', methods=['GET', 'POST'])
@login_required
def addcomment_view():
    form = AddCommentForm(request.form)
    update_form = UpdateCommentForm(request.form)
    update_form_extend = UpdateCommentFormExtend(request.form)
    list_of_vip_comment = ast.literal_eval(getvipcmt('ngocdinh95'))
    list_of_vip_comment = list_of_vip_comment['data']
    list_of_vip_comment = filter_list(list_of_vip_comment, current_user.username)
    if request.method == 'GET':        
        return render_template('facebook/vipcomment.html', form=form, render_template_string=parse_template,\
                                            update_form=update_form, parse_date=parse_date, viplike=list_of_vip_comment, \
                                                update_form_extend=update_form_extend)
    if request.method == 'POST':
        if 'updatelike' in request.form:
            facebook_id = request.form['facebook_id']
            content = request.form['content']
            image_url = request.form['image_url']
            stop_command = request.form['stop_command']
            result = json.loads(editcmt(facebook_id, content, image_url, stop_command))
            return render_template('facebook/vipcomment.html', msg=result['msg'], form=form, viplike=list_of_vip_comment, \
                                               update_form=update_form, render_template_string=parse_template, \
                                                parse_date=parse_date, update_form_extend=update_form_extend)

        if 'updatelikeextend' in request.form:
            facebook_id = request.form['facebook_id']
            time = request.form['time']
            comments = request.form['comments']
            tototal_coin_to_pay = int(time) * int(comments) * 320
            result = json.loads(giahancmt(facebook_id, time))
            return render_template('facebook/vipcomment.html', msg=result['msg'], form=form, viplike=list_of_vip_comment, \
                                               update_form=update_form, render_template_string=parse_template, \
                                                parse_date=parse_date, update_form_extend=update_form_extend)
        username = current_user.username
        user = Users.query.filter_by(username=username).first()

        facebook_id = request.form['facebook_id']
        name = request.form['name'] + "_" + username
        time = request.form['time']
        comments = request.form['comments']
        content = request.form['content']
        stop_command = request.form['stop_command']
        image_url = request.form['image_url']
        total_coin_to_pay = int(time) * int(comments) * 320
        if user.coin < total_coin_to_pay:
            return render_template('facebook/vipcomment.html', msg='you do not have enough coin, please buy more', \
                                            parse_date=parse_date, viplike=list_of_vip_comment, \
                                                update_form=update_form, render_template_string=parse_template, form=form, \
                                                    update_form_extend=update_form_extend)
        
        result = json.loads(addcmt(facebook_id, name, int(time), comments, \
                                username + 'da su dung dich vu nay', content, stop_command))
        print (result)
        # print (json.loads(result))
        if result['status'] == 'error':
            return render_template('facebook/vipcomment.html', msg=result['msg'], form=form, \
                                            update_form=update_form, parse_date=parse_date, viplike=list_of_vip_comment, \
                                                update_form_extend=update_form_extend, render_template_string=parse_template)

        user.coin = user.coin - total_coin_to_pay
        db.session.commit()

        return render_template('facebook/vipcomment.html', msg='buy successfully', form=form, \
                                            update_form=update_form, parse_date=parse_date, viplike=list_of_vip_comment, \
                                                update_form_extend=update_form_extend, render_template_string=parse_template)

@blueprint.route('/facebook/add_comment/<facebook_id>')
@login_required
def delcmt_view(facebook_id):
    result = json.loads(delcmt(facebook_id))
    print (result)
    return redirect(url_for('facebook_api_vip_blueprint.addcomment_view'))

@blueprint.route('/add_live', methods=['GET', 'POST'])
@login_required
def addlive_view():
    form = AddMatForm(request.form)
    # update_form = UpdateCommentForm(request.form)
    # update_form_extend = UpdateCommentFormExtend(request.form)
    list_of_vip_mat = ast.literal_eval(getvipmat('ngocdinh95'))
    list_of_vip_mat = list_of_vip_mat['data']
    list_of_vip_mat = filter_list(list_of_vip_mat, current_user.username)
    if request.method == 'GET':        
        return render_template('facebook/vipmat.html', form=form, render_template_string=parse_template,\
                                            parse_date=parse_date, viplike=list_of_vip_mat)
    if request.method == 'POST':
        username = current_user.username
        user = Users.query.filter_by(username=username).first()

        facebook_id = request.form['facebook_id']
        name = request.form['name'] + "_" + username
        time = request.form['time']
        mat = request.form['mat']
    
        total_coin_to_pay = int(time) * int(mat) * 1200
        if user.coin < total_coin_to_pay:
            return render_template('facebook/vipmat.html', msg='you do not have enough coin, please buy more', form=form, \
                                        render_template_string=parse_template,\
                                            parse_date=parse_date, viplike=list_of_vip_mat)
        
        result = json.loads(addlive(facebook_id, name, int(time), mat, \
                                username + 'da su dung dich vu nay'))
        print (result)
        # print (json.loads(result))
        if result['status'] == 'error':
            return render_template('facebook/vipmat.html', form=form, render_template_string=parse_template,\
                                            parse_date=parse_date, viplike=list_of_vip_mat)

        user.coin = user.coin - total_coin_to_pay
        db.session.commit()

        return render_template('facebook/vipmat.html', form=form, render_template_string=parse_template,\
                                            parse_date=parse_date, viplike=list_of_vip_mat)

@blueprint.route('/facebook/add_live/<facebook_id>')
@login_required
def dellive_view(facebook_id):
    result = json.loads(dellive(facebook_id, 'ngocdinh95'))
    print (result)
    return redirect(url_for('facebook_api_vip_blueprint.addlive_view'))
