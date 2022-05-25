
from apps import db
from apps.authentication.models import Users 
# from apps.authentication.util import hash_pass

class transactions(db.Model):

    __tablename__ = 'transactions'

    transaction_id = db.Column(db.Integer, primary_key=True)
    money = db.Column(db.String(64))
    phone_number = db.Column(db.Integer)
    username = db.Column(db.String(64), db.ForeignKey('Users.username'))
    # user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    
    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            setattr(self, property, value)
    
    def __repr__(self):
        return str(self.ecg_file_name)