from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
## importar do database a classe que vai ser o usuario ("from greenvolt.models import User/Usuario")

class CadastroForm(FlaskForm):
    ## implentar código de verificação se o usuario existe no db
    ## implentar código de verificação se o email é existente no db

    usuario = StringField(label="Nome de Usuário", validators=[DataRequired()] ) ## definir com o grupo quaisvão ser os parametros minimos para criação do usuario
    email = StringField(label="Email", validators=[DataRequired() ,Email()])
    senha1 = PasswordField(label="Senha", validators=[DataRequired()]) ## definir com o grupo os parametros para a senha
    senha1 = PasswordField(label="Confirmação de Senha", validators=[DataRequired(), EqualTo(senha1)])
    submit = SubmitField(label="Cadastrar")


class LoginForm(FlaskForm):
    usuario = StringField(label="Usuário:", validators=[DataRequired()])
    senha = PasswordField(label="Senah:", validators=[DataRequired()])
    submit = SubmitField(label="Login")
