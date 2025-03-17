from app import create_app
from app.models import Local

app = create_app()

with app.app_context():
    locais = Local.query.all()
    print("LISTAGEM DE LOCAIS CADASTRADOS:")
    for local in locais:
        print(f"Nome: {local.nome} | Latitude: {local.latitude} | Longitude: {local.longitude}")
