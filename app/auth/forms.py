from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User
from flask_wtf import FlaskForm
from wtforms import(
    PasswordField,
    StringField,
    SubmitField,
    ValidationError
)


class RegistrationForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    user = StringField("Usuário", validators=[DataRequired()])
    full_name = StringField("Nome Completo", validators=[DataRequired()])
    password =PasswordField("Senha", validators=[DataRequired(), EqualTo("password2")])
    password2 = PasswordField("Confirme a senha")
    submit = SubmitField("Cadastrar")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("E-mail já utilizado.Escolha outro ou faça login!")

    def validate_login(self, login):
        login = Login.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError("Usuário já utilizado.Escolha outro ou faça login!")


class LoginForm(FlaskForm):
    login = StringField("E-mail ou usuário", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Login")