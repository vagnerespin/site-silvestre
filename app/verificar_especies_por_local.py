
from app import create_app
from app.models import Local

app = create_app()
with app.app_context():
    locais = Local.query.all()
    for local in locais:
        print(f"Local: {local.nome}")
        print("Espécies associadas:")
        for especie in local.especies:
            print(f" - {especie.nome_comum} ({especie.nome_cientifico})")
        print("-" * 40)
