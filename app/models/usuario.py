from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .. import login_manager


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nomeCompleto = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True, index=True)
    senha_hash = db.Column(db.String(128))

    @property
    def senha(self):
        raise AttributeError('senha não é legível para mortais')

    @senha.setter
    def senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))