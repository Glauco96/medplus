import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRETE_KEY = os.environ.get("SECRETE_KEY") or 'timão2020'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "database.db")
    SQLTRALCHEMY_TRACK_MODIFICATIONS = False
    PAGINATION = 10
    