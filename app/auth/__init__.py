from flask import blueprint

auth =  Blueprint("auth", __name__)

from . import views