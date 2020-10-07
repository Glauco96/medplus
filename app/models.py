from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from datetime import datetime


class Admin(db.Model):

    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return 'Admin: {}\nUser ID: {}'.format(self.id, self.user_id)

    
class Secretary(db.Model):

    __tablename__ = "secretaries"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    consult_id = db.Column(db.Integer, db.ForeignKey('consults.id'))

    def __repr__(self):
        return 'Secretary: {}'.format(self.id)


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    login = db.Column(db.String(60), index=True, unique=True)
    full_name = db.Column(db.String(50), index=True)
    password = db.Column(db.String(128))
    email_confirmed = db.Column(db.Boolean, default=False)
    admins = db.relationship('Admin', backref='user', lazy='dynamic')
    secretaries = db.relationship('Secretary', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
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
    id_patient = db.Column(db.Integer, db.ForeignKey('patients.id'))
    id_status_consult = db.Column(db.Integer, db.ForeignKey('status_consults.id'))

    def __repr__(self):
        return 'Consult ID: {}\nConsult date: {}\nPatient: {}\nStatus Consult: {}'.format(self.id,
                                                                                          self.consult_date,
                                                                                          self.id_patient,
                                                                                          self.id_status_consult)


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
    id_consult = db.Column(db.Integer, db.ForeignKey('consults.id'))
    id_specialty = db.Column(db.Integer, db.ForeignKey('specialties.id'))

    def __repr__(self):
        return 'Doctor ID: {}\nDoctor Name: {}'.format(self.id, self.full_name)


class OccupationArea(db.Model):

    __tablename__ = 'occupation_areas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, index=True)
    id_specialty = db.Column(db.Integer, db.ForeignKey('specialties.id'))

    def __repr__(self):
        return 'OccupationArea ID: {}\nOccupation: {}'.format(self.id, self.name)


class Specialty(db.Model):

    __tablename__ = 'specialties'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, index=True)
    doctors = db.relationship('Doctor', backref='doctors_specialty', lazy="dynamic")
    occupation_areas = db.relationship('OccupationArea', backref='occupation_areas_specialties', lazy="dynamic")

    def __repr__(self):
        return 'Specialty ID: {}\nSpecialty: {}'.format(self.id, self.name)


class Patient(db.Model):
    
    __tablename__ = 'patients'
    
    id = db.Column(db.Integer, primary_key=True)
    consults = db.relationship('Consult', backref="patient", lazy="dynamic")

    def __repr__(self):
        return 'Patient ID: {}\nPatient Name: {}'.format(self.id, self.full_name)


