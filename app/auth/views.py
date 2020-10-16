from flask import flash, redirect, render_template, url_for
from flask_login import login_user
from .forms import RegistrationForm, LoginForm
from app import db
from app.models import User
from . import auth


@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(
                email=form.email.data,
                login=form.user.data,
                full_name=form.full_name.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('auth.login'))
        except Exception:
            flash(e, 'error')
            db.session.rollback()
        finally:
            db.session.close()
    return render_template('auth/register.html', form=form, tittle='Cadastrar')


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if not user:
            user = User.query.filter_by(email=form.login.data).firts()
        if user and user.verify_password(form.password.data):
            login_user(user) 
            return redirect(url_for('home.dashboard'))  
        flash('Usuário ou senha inválidos', 'error')
    return render_template('auth/login.html', form=form, tittle="Login")