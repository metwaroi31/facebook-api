
from apps import db
from apps.authentication.models import Users 
# from apps.authentication.util import hash_pass

class ECGs(db.Model):

    __tablename__ = 'ECGs'

    id = db.Column(db.Integer, primary_key=True)
    facebook_id = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    
    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            # if hasattr(value, '__iter__') and not isinstance(value, str):
            #     # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
            #     value = value[0]

            # if property == 'password':
            #     value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)
    
    def __repr__(self):
        return str(self.ecg_file_name)