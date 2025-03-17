from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .models import db, Usuario

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.senha == senha:
            login_user(usuario)
            return redirect(url_for('main.index'))
        else:
            flash('Credenciais inválidas.')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if Usuario.query.filter_by(email=email).first():
            flash('Usuário já existe.')
        else:
            novo_usuario = Usuario(email=email, senha=senha)
            db.session.add(novo_usuario)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('cadastro_usuario.html')
