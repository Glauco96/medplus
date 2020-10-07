from flask import blueprint

main =  Blueprint("main", __name__)

from . import views