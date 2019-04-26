from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class cadastroRestauranteForm(FlaskForm):
    nome = StringField("Nome do Restaurante", validators=[DataRequired()])
    endereco = StringField("Endereço", validators=[DataRequired()])
    numero = StringField("Numero do restaurante", validators=[DataRequired()])
    tel = StringField("Numero de telefone", validators=[DataRequired()])
    submit = SubmitField("Cadastre")