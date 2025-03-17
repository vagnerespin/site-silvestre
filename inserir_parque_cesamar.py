from app import create_app, db
from app.models import Local

app = create_app()

with app.app_context():
    nome = "Parque Cesamar"
    descricao = "Parque com rica fauna de espécies silvestres"
    latitude = -10.209744
    longitude = -48.324348

    # Verificar se o local já existe
    local_existente = Local.query.filter_by(nome=nome).first()

    if local_existente:
        print("✅ O local 'Parque Cesamar' já está cadastrado no banco de dados.")
    else:
        novo_local = Local(nome=nome, descricao=descricao, latitude=latitude, longitude=longitude)
        db.session.add(novo_local)
        db.session.commit()
        print("✅ Parque Cesamar adicionado com sucesso ao banco de dados!")
