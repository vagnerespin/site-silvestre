from app import create_app, db
from app.models import Especie, Local

app = create_app()

with app.app_context():
    especies = Especie.query.all()
    if especies:
        print("Espécies encontradas no banco de dados:")
        for especie in especies:
            print(f"Nome comum: {especie.nome_comum} | Científico: {especie.nome_cientifico} | Local ID: {especie.local_id}")
    else:
        print("Nenhuma espécie encontrada.")
