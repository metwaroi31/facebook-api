from apps.authentication.models import Users
import datetime
from apps import db, login_manager

def create_admin(username):
    user = Users(username=username, email="admin@yopmail.com", password="!@#$%^&*()")
    # user.confirmed = True
    # user.confirmed_on = datetime.datetime.now()
    user.is_admin = True
    db.session.add(user)
    db.session.commit()

def hash_pass(username):
    """Hash a password for storing."""

    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', username.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash)  # return bytes
