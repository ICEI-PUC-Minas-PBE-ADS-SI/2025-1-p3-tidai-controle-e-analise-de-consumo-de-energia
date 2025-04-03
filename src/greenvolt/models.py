from greenvolt import db
from greenvolt import bcrypt
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100), nullable=False, unique=False)
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    senha = db.Column(db.String(length=255), nullable=False, unique=True)

    dispositivos = db.relationship('Dispositivo', backref='usuario', lazy=True)
    contas = db.relationship('Conta', backref='usuario', lazy=True)
    noticias = db.relationship('Noticia', backref='usuario', lazy=True)

    @property
    def senhacrip(self):
        return self.senhacrip
    
    @senhacrip.setter
    def senhacrip(self, senha_texto):
        self.senha = bcrypt.generate_password_hash(senha_texto).decode('utf-8')

    def converte_senha(self, senha_texto_claro):
        return bcrypt.check_password_hash(self.senha, senha_texto_claro)


class Dispositivo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100), nullable=False)
    potencia_watts = db.Column(db.Float, nullable=False)
    tempo_uso = db.Column(db.Float, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_ref = db.Column(db.String(length=7), nullable=False, unique=True)
    valor = db.Column(db.Numeric(10,2), nullable=False)
    consumo_kwh = db.Column(db.Integer, nullable=False)
    ## Nao vou colocar data de vencimento
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(length=255), nullable=False, unique=True)
    url = db.Column(db.String(length=255), nullable=False, unique=True)
    data_salva = db.Column(db.String(length=255), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)