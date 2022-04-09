from flask import Blueprint

blueprint = Blueprint(
    'google_service_blueprint',
    __name__,
    url_prefix=''
)
