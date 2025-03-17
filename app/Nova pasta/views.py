from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app.models import Local, Especie
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    locais = Local.query.all()
    return render_template('index.html', locais=locais)

@main.route('/listar_especies')
def listar_especies():
    local_id = request.args.get('local_id', type=int)
    locais = Local.query.all()
    if local_id:
        especies = Especie.query.filter_by(local_id=local_id).all()
    else:
        especies = Especie.query.all()
    return render_template('listar_especies.html', especies=especies, locais=locais)

@main.route('/cadastrar_local', methods=['GET', 'POST'])
@login_required
def cadastrar_local():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        novo_local = Local(nome=nome, descricao=descricao, latitude=latitude, longitude=longitude)
        db.session.add(novo_local)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('cadastrar_local.html')

@main.route('/add_especie', methods=['GET', 'POST'])
@login_required
def add_especie():
    locais = Local.query.all()
    if request.method == 'POST':
        nome_comum = request.form['nome_comum']
        nome_cientifico = request.form['nome_cientifico']
        descricao = request.form['descricao']
        imagem_url = request.form['imagem_url'] or 'img/default.jpg'
        local_id = request.form['local_id']
        nova_especie = Especie(nome_comum=nome_comum, nome_cientifico=nome_cientifico,
                               descricao=descricao, imagem_url=imagem_url, local_id=local_id)
        db.session.add(nova_especie)
        db.session.commit()
        return redirect(url_for('main.listar_especies'))
    return render_template('add_especie.html', locais=locais)

@main.route('/dashboard')
@login_required
def dashboard():
    especies = Especie.query.all()
    locais = Local.query.all()
    return render_template('dashboard.html', especies=especies, locais=locais)
