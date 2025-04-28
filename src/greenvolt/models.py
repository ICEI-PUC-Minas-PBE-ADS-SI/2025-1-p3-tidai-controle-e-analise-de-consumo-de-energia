from greenvolt import db, login_manager
from greenvolt import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100), nullable=False, unique=False)
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    senha = db.Column(db.String(length=255), nullable=False, unique=False)

    dispositivos = db.relationship('Dispositivo', backref='usuario', lazy=True)
    contas = db.relationship('Conta', backref='usuario', lazy=True)
    noticias = db.relationship('Noticia', backref='usuario', lazy=True)

    @property
    def senhacrip(self):
        return self.senha
    
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
    data_ref = db.Column(db.Date, nullable=False, unique=False)
    valor = db.Column(db.Numeric(10,2), nullable=False)
    consumo_kwh = db.Column(db.Integer, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def requisitos_para_adicionar(self,usuario):
        conta_existente = Conta.query.filter_by(usuario_id=usuario.id, data_ref=self.data_ref).first()
        return not conta_existente and self.valor > 0

    def adicionar_conta(self, usuario):
        self.usuario_id = usuario.id
        db.session.add(self)
        db.session.commit()

    @classmethod
    def remover_conta(cls, usuario, data_ref):
        conta = cls.query.filter_by(
            usuario_id=usuario.id,
            data_ref=data_ref
        ).first()
        
        if not conta:
            return False
            
        try:
            db.session.delete(conta)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise


class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(length=255), nullable=False, unique=True)
    url = db.Column(db.String(length=255), nullable=False, unique=True)
    data_salva = db.Column(db.String(length=255), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)