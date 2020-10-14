from flask import flash, redirect, render_template, url_for
from .forms import RegistrationForm
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
        except:
            flash('Cadastro não realizado. Tente novamente!', 'error')
            db.session.rollback()
        finally:
            db.session.close()
    return render_template('auth/register.html', fomr=form, tittle='Cadastrar')

