from flask import render_template, request, url_for, redirect
from flask_login import login_user
from . import auth
from .forms import LoginForm
from ..models import Usuario

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario is not None and usuario.verificar_senha(form.senha.data):
            login_user(usuario)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        # flash('') ME COBREM
    return render_template('auth/login.html', form=form)


    return render_template('auth/login.html')