
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models import Local, Especie
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    local_cesamar = Local.query.filter_by(nome="Parque Cesamar").first()
    especies = Especie.query.filter_by(local_id=local_cesamar.id).all() if local_cesamar else []
    return render_template("index.html", especies_cesamar=especies)

@main.route('/listar_locais')
def listar_locais():
    locais = Local.query.all()
    return render_template('listar_locais.html', locais=locais)

@main.route('/listar_especies')
def listar_especies():
    local_id = request.args.get('local_id')
    locais = Local.query.all()
    if local_id:
        especies = Especie.query.filter_by(local_id=local_id).all()
    else:
        especies = Especie.query.all()
    return render_template('listar_especies.html', especies=especies, locais=locais)

@main.route('/add_especie', methods=['GET', 'POST'])
def add_especie():
    if request.method == 'POST':
        nome_comum = request.form['nome_comum']
        nome_cientifico = request.form['nome_cientifico']
        descricao = request.form['descricao']
        imagem_url = request.form['imagem_url']
        local_id = request.form['local_id']

        nova_especie = Especie(
            nome_comum=nome_comum,
            nome_cientifico=nome_cientifico,
            descricao=descricao,
            imagem_url=imagem_url,
            local_id=local_id
        )
        db.session.add(nova_especie)
        db.session.commit()
        return redirect(url_for('main.listar_especies'))

    locais = Local.query.all()
    return render_template('add_especie.html', locais=locais)

@main.route('/cadastrar_local', methods=['GET', 'POST'])
def cadastrar_local():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        novo_local = Local(nome=nome, descricao=descricao)
        db.session.add(novo_local)
        db.session.commit()
        return redirect(url_for('main.listar_locais'))
    return render_template('cadastrar_local.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
