# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')
    SECURITY_PASSWORD_SALT = config('SECURITY_PASSWORD_SALT', default='To0pS3crEt_007')
    # DEBUG = True
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    # MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    # MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

    # mail accounts
    MAIL_DEFAULT_SENDER = 'from@example.com'

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # google service 
    # CLIENT_ID = "331960905561-61rn63sciv8flf59ru113mds69nufaon.apps.googleusercontent.com"
    AUTHENTICATION_SERVICE_ID = "oesauniusdfniuhaeoapidpcneoisnfg"

    # google oauth service
    ACCESS_TOKEN_URI = 'https://www.googleapis.com/oauth2/v4/token'
    AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&prompt=consent'

    AUTHORIZATION_SCOPE ='openid email profile'

    AUTH_REDIRECT_URI = "http://e80f-14-187-50-127.ngrok.io/google/auth"
    BASE_URI = "http://e80f-14-187-50-127.ngrok.io/"
    CLIENT_ID = "331960905561-p7d5aq8plnqjcscc74lf29tl0ah1cspu.apps.googleusercontent.com"
    CLIENT_SECRET = "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"
    AUTH_TOKEN_KEY = 'auth_token'
    AUTH_STATE_KEY = 'auth_state'

    # GRAPH API 
    APP_ID = '3152695414975029'
    ACCESS_TOKEN = 'EAAszXBpLajUBAJQmk3ooA5Qbr3VYSoxpHbc5ZAvdEEXyAZAW6R9qqRVCowFtCNDcZAkOeF67F3IbLuuAX8LOHPeNYcUNQXTx1N7XuFIKL3hEpnJINqWmtM0NXFOyzZCi6t3w1ZBhpz8lq2Kr0ub0tiM9TjkMxvsLTZBfFj5oiuoOrfYFAZBGKTGZCnjZBTOR2uyTNlE80nCILEUaLOkfdgDRKSfo4KwGFNLAg9JNwYVuspSUR85TAAN2B'

    # FACEBOOK API
    FACEBOOK_API_KEY = '89bd8ef4fa4d9951407087c891ee61da'
    FACEBOOK_API = 'http://api.viplike.me/likenew.php'
    FACEBOOK_API_CMT = 'http://api.viplike.me/cmt.php'
    FACEBOOK_API_MAT = 'http://api.viplike.me/mat.php'
    FACEBOOK_API_BUFF = 'http://api.viplike.me/buff.php'

class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='postgresql'),
        config('DB_USERNAME', default='appseed'),
        config('DB_PASS', default='pass'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=5432),
        config('DB_NAME', default='appseed-flask')
    )
    FACEBOOK_API_KEY = '89bd8ef4fa4d9951407087c891ee61da'
    FACEBOOK_API = 'http://api.viplike.me/likenew.php'
    FACEBOOK_API_CMT = 'http://api.viplike.me/cmt.php'
    FACEBOOK_API_MAT = 'http://api.viplike.me/mat.php'

class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
