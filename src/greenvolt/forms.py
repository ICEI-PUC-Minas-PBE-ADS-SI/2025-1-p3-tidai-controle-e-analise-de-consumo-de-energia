from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, DecimalField, HiddenField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from greenvolt.models import Usuario
import re


class CadastroForm(FlaskForm):

    def validate_usuario(self, check_user):
        user =  Usuario.query.filter_by(nome=check_user.data).first()
        if user:
            raise ValidationError("Usuário ja existe ! Cadastre outro nome de usuário")

    def validate_email(self, check_email):
        email =  Usuario.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Email ja cadastrado ! Cadastre outro email")

    def validate_senha(self, check_senha):
        senha = Usuario.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError("Usuário ja existe ! Cadastre outro nome de usuário")
        

    nome = StringField(label="Nome de Usuário", validators=[DataRequired(), Length(min=6, max=30)] ) ## definir com o grupo quaisvão ser os parametros minimos para criação do usuario
    email = StringField(label="Email", validators=[DataRequired() ,Email()])
    senha1 = PasswordField(label="Senha", validators=[DataRequired()]) ## definir com o grupo os parametros para a senha
    senha2 = PasswordField(label="Confirmação de Senha", validators=[DataRequired(), EqualTo('senha1')])
    submit = SubmitField(label="Cadastrar")


class LoginForm(FlaskForm):
    email = StringField(label="Email:", validators=[DataRequired()])
    senha = PasswordField(label="Senha:", validators=[DataRequired()])
    submit = SubmitField(label="Login")

class AdicionarContaForm(FlaskForm):
    data = DateField('Data de Referência', format='%Y-%m', validators=[DataRequired()])
    valor = DecimalField('Valor', validators=[DataRequired()])
    consumo_kwh = DecimalField('Consumo (kWh)', validators=[DataRequired()])
    submit = SubmitField(label="Adicionar Conta")

class RemoverContaForm(FlaskForm):
    data_ref = HiddenField(validators=[DataRequired()])
    submit = SubmitField(label="Remover conta")
