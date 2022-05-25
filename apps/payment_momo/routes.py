# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from apps import db
from apps.payment_momo import blueprint
from flask import render_template, request
from flask_login import login_required, current_user
from apps.authentication.models import Users
from apps.payment_momo.forms import PayMomoForm, GetOTPForm, AddMomoForm

@blueprint.route('/pay_momo')
@login_required
def pay_momo():
    form = PayMomoForm(request.form)
    if current_user.is_admin == False:
        return render_template('home/index.html', user=current_user, segment='index')
    if current_user.is_admin == True:
        users = Users.query.all()
        for user in users:
            print (user)
        return render_template('home/index_admin.html', users=users, segment='index')


@blueprint.route('/get_otp')
@login_required
def get_otp():
    form = GetOTPForm
    if current_user.is_admin == False:
        return render_template('home/index.html', user=current_user, segment='index')
    if current_user.is_admin == True:
        users = Users.query.all()
        for user in users:
            print (user)
        return render_template('home/index_admin.html', users=users, segment='index')

@blueprint.route('/get_token')
@login_required
def get_token():
    if current_user.is_admin == False:
        return render_template('home/index.html', user=current_user, segment='index')
    if current_user.is_admin == True:
        users = Users.query.all()
        for user in users:
            print (user)
        return render_template('home/index_admin.html', users=users, segment='index')
