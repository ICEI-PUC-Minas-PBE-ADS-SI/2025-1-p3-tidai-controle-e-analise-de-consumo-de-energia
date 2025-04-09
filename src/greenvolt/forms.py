from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from greenvolt.models import Usuario
import re


class CadastroForm(FlaskForm):

    def validate_usuario(self, check_user):
        user =  Usuario.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuário ja existe ! Cadastre outro nome de usuário")

    def validate_email(self, check_email):
        email =  Usuario.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Email ja cadastrado ! Cadastre outro email")

    def validate_senha(self, senha1):
        senha = senha1.data
        if not re.search(r'[A-Z]', senha) or \
            not re.search(r'[a-z]', senha) or \
            not re.search(r'[\d]', senha) or \
            not re.search(r'[!@#$%^&*(),.?":;{}|<>/]', senha):
                raise ValidationError('A senha deve conter pelo menos 1 letra maiúscula, 1 letra minúscula, 1 número e 1 caractere especial.')
        ##if senha:
        ##    raise ValidationError("Usuário ja existe ! Cadastre outro nome de usuário")
        

    usuario = StringField(label="Nome de Usuário", validators=[DataRequired(), Length(min=6, max=30)] ) ## definir com o grupo quaisvão ser os parametros minimos para criação do usuario
    email = StringField(label="Email", validators=[DataRequired() ,Email()])
    senha1 = PasswordField(label="Senha", validators=[DataRequired()]) ## definir com o grupo os parametros para a senha
    senha1 = PasswordField(label="Confirmação de Senha", validators=[DataRequired(), EqualTo(senha1)])
    submit = SubmitField(label="Cadastrar")


class LoginForm(FlaskForm):
    email = StringField(label="Email:", validators=[DataRequired()])
    senha = PasswordField(label="Senha:", validators=[DataRequired()])
    submit = SubmitField(label="Login")
