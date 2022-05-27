# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from apps.authentication.models import Users

@blueprint.route('/index')
@login_required
def index():
    if current_user.is_admin == False:
        return render_template('home/index.html', user=current_user, segment='index')
    if current_user.is_admin == True:
        users = Users.query.all()
        for user in users:
            print (user)
        return render_template('home/index_admin.html', users=users, segment='index')

# @blueprint.route('/index_admin')
# @login_required
# def index_admin():
#     print ("going to admin page")
#     return render_template('home/index_admin.html', segment='index')
@blueprint.route('/<template>')
# @login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except Exception as e:
        print (e)
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
