# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_migrate import Migrate
from sys import exit
from decouple import config
from flask_mail import Mail 
from apps.config import config_dict
from apps import create_app, db
from apps.admin.util import create_admin
from apps.payment_momo.utils import pay_momo
import click
# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)

@app.cli.command("pay-user")
def pay_user():
    pay_momo()

@app.cli.command("create-user")
@click.argument("username")
def create_user(username):
    create_admin(username)

def get_mail_flask ():
    mail = Mail(app)
    mail.init_app(app)
    return mail

# mail  = Mail
if DEBUG:
    app.logger.info('DEBUG       = ' + str(DEBUG))
    app.logger.info('Environment = ' + get_config_mode)
    app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI)

if __name__ == "__main__":
    try :
        app.run(use_reloader=True, threaded=True)
    except Exception as err:
        print (err)