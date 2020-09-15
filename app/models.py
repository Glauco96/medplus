from flask_login import UserMixing
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from datetime import datetime


class Admin(db.Model):

    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeingKey('users.id'))

    def __repr__(self):
        return 'Admin: {}\n User ID:'.format(self.id, self.user_id)


class Secretary(db.Model):

    __tablename__ = "secretaries"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeingKey('users.id'))
    consult_id = db.Column(db.Integer, db.ForeingKey('consults.id'))

    def __repr__(self):
        return 'Secretary: {}'.format(self.id)


class User(UserMixing, db.Model) :

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    login = db.Column(db.String(60), index=True, unique=True)
    full_name = db.Column(db.String(60), index=True)
    password = db.Column(db.String(120))
    email_confirmed = db.Column(db.Boolean, default=False)
    admins = db.relationship('Admin', backref='user', lazy='dynamic')
    secretaries = db.relationship('Secretary', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password = gerenate_password_hash(password)

    def verify_passwrod(self, password):
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
    id_patient = db.Column(db.Integer, db.ForeingKey('patients.id'))
    id_status_consult = db.Column(db.Integer, db.ForeingKey('status_consults.id'))

    def __repr__(self):
        return 'User ID: {}\nConsult date: {}'.format(self.id, self.consult_date)


class StatusConsult(db.Model):

    __tablename__ = "status_consults"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True)
    consults = db.relationship('Consult', backref='status_consult', lazy='dynamic')

    def __repr__(self):
        return 'StatusConsult ID: {}\nStatus: {}'.format(self.id, self.status)

class Doctor(db.Model):
    
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), index=True) 
    id_consult = db.Column(db.Integer, db.ForeingKey('consults.id'))
    id_specialty = db.Column(db.Integer, db.ForeingKey('specialties.id'))


    
    def __repr__(self):
        return 'User ID: {}\Doctor Name: {}'.format(self.id, self.full_name)


class OccupationArea(db.Model):

    __tablename__ = 'ocuppation_areas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, index=True)
    id_specialty = db.Column(db.Integer, db.ForeingKey('specialties.id'))


    def __repr__(self):
        return 'OccupationArea ID: {}\Occupation Name: {}'.format(self.id, self.name)


class Specialty(db.Model):

    __tablename__ = 'specialties'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, index=True)
    doctors = db.relationship('Doctor', backref='doctors_specialty', lazy="dynamic")
    occupation_areas = db.relationship('OccupatonArea', backref='occupation_areas_specialties', lazy="dynamic")

    def __repr__(self):
        return 'Specialty ID: {}\Specialty Name: {}'.format(self.id, self.name)


class Patient(db.Modcel):
    
     __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), index=True)
    consults = db.relationship('Consult', backref='patient', lazy="dynamic")


    def __repr__(self):
        return 'User ID: {}\Patient Name: {}'.format(self.id, self.full_name)