from flask import blueprint

admin =  Blueprint("admin", __name__)

from . import views