from . import main
from flask import render_template
from flask_login import login_required
from .forms import cadastroRestauranteForm

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/cadastreRestaurante', methods=['GET', 'POST'])
@login_required
def cadastreRestaurante():
    form = cadastroRestauranteForm()
    return render_template('cadastreRestaurante.html', form=form)


@main.route('/pessoa')
@login_required
def natalia():
    return "oi natalia"
