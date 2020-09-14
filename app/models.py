from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, url_for
from app import db, login
from datetime import datetime
import os


class Admin(db.Model):

    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeingKey('users.id'))

    def __repr__(self):
        return 'Admin: {}'.format(self.id)


class Secretary(db.Model):

    __tablename__ = "secretaries"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeingKey('users.id'))
    consult_id = db.Column(db.Integer, db.ForeingKey('cpnsults.id'))

    def __repr__(self):
        return 'Secretary: {}'.format(self.id)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    login = db.Column(db.String(60), index=True, unique=True)
    full_name = db.Column(db.String(60), index=True)
    password = db.Column(db.String(120))
    email_confirmed = db.Column(db.Boolean, default=False)
    admins = db.relationship('Admin', backref='user', lazy='dynamic')
    secretaries = db.relationship('Secretary', backref='user', lazy='dynamic')

    def set_password(self, password)
        self.password = gerenate_password_hash(password)

    def verify_passwrod(self, password)
        return check_password_hash(self.password, password)

    def __repr__(self):
        return 'User ID: {}\nUser Name: {}'.format(self.id, self.full_name)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Consult(db.Model):

    __tablename__ = "consults"

    id = db.Column(db.Integer, primary_key=True)
    consult_date = db.Column(db.DateTime, default=datetime.utcnow)
    secretaries = db.relationship('Secretary', backref='consult', lazy='dynamic')
    doctors = db.relationship('Doctor', backref='consult', lazy='dynamic')
    patients = db.relationship('Patient', backref='cpontul', lazy='dynamic')


     def __repr__(self):
        return 'User ID: {}\nConsult date: {}'.format(self.id, self.consult_date)