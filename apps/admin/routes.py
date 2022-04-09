from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)
import datetime
from apps import db, login_manager
from apps.admin import blueprint
from apps.authentication.models import Users
from apps.admin.util import *
import datetime
import click
from apps.admin.forms import UserForm
# Login & Registration

@blueprint.route('/profile/<username>', methods=['GET', 'POST'])
def profile_view(username):
    form = UserForm()
    if current_user.is_admin:
        user = Users.query.filter_by(username=username).first()
        if request.method == 'POST':
            coin = request.form['coin']
            user.coin = coin
            db.session.commit()
            return redirect(url_for('authentication_blueprint.route_default'))
        return render_template('home/profile.html', user=user, form=form)
