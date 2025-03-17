from flask import Blueprint, render_template, jsonify
from app.models import Local, Especie

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/especies/<int:local_id>')
def especies_por_local(local_id):
    local = Local.query.get(local_id)
    if not local:
        return jsonify({'erro': 'Local não encontrado'}), 404

    especies = Especie.query.filter_by(local_id=local_id).all()
    especies_data = []
    for especie in especies:
        especies_data.append({
            'nome_comum': especie.nome_comum,
            'nome_cientifico': especie.nome_cientifico,
            'descricao': especie.descricao,
            'imagem_url': especie.imagem_url
        })

    return jsonify({'local': local.nome, 'especies': especies_data})
from flask import render_template

@app.route('/cadastrar_local')
def cadastrar_local():
    return render_template('cadastrar_local.html')
