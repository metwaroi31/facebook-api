from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)
import datetime
from apps import db, login_manager
from apps.google_service import blueprint
from apps.google_service.authentication import *
import datetime
from apps.authentication.models import Users

@blueprint.route('/google/logout')
@no_cache
def logout():
    flask.session.pop(AUTH_TOKEN_KEY, None)
    flask.session.pop(AUTH_STATE_KEY, None)

    return flask.redirect(BASE_URI, code=302)