from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import db, Local, Especie

main = Blueprint('main', __name__)

@main.route('/')
def index():
    locais_raw = Local.query.all()
    locais = []
    for local in locais_raw:
        locais.append({
            'id': local.id,
            'nome': local.nome,
            'descricao': local.descricao,
            'latitude': local.latitude,
            'longitude': local.longitude,
            'especies': [{'id': e.id, 'nome': e.nome} for e in local.especies]
        })
    return render_template('index.html', locais=locais)

@main.route('/listar_especies')
def listar_especies():
    especies = Especie.query.all()
    return render_template('listar_especies.html', especies=especies)

@main.route('/cadastrar_especie', methods=['GET', 'POST'])
@login_required
def cadastrar_especie():
    locais = Local.query.all()
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        local_id = request.form['local_id']
        especie = Especie(nome=nome, descricao=descricao, local_id=local_id)
        db.session.add(especie)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('cadastro_especie.html', locais=locais)

@main.route('/cadastrar_local', methods=['GET', 'POST'])
@login_required
def cadastrar_local():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        local = Local(nome=nome, descricao=descricao, latitude=latitude, longitude=longitude)
        db.session.add(local)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('cadastro_local.html')
