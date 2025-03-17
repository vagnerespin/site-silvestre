from app import create_app
from app.models import db, Local, Especie

app = create_app()
with app.app_context():
    # Verificar se o Parque Cesamar já existe
    cesamar = Local.query.filter_by(nome="Parque Cesamar").first()
    if not cesamar:
        cesamar = Local(
            nome="Parque Cesamar",
            descricao="Principal parque urbano de Palmas, habitat de diversas espécies.",
            latitude=-10.2046,
            longitude=-48.3349
        )
        db.session.add(cesamar)
        db.session.commit()
        print("Local 'Parque Cesamar' criado.")

    especies_cesamar = [
        {"nome": "Arara", "descricao": "Ave colorida da fauna brasileira, símbolo da mata tropical."},
        {"nome": "Capivara", "descricao": "Maior roedor do mundo, muito comum em áreas alagadas."},
        {"nome": "Mucura", "descricao": "Marsupial brasileiro conhecido por sua agilidade."},
        {"nome": "Jaboti", "descricao": "Réptil terrestre de casco resistente, comum no Cerrado."},
        {"nome": "Jibóia", "descricao": "Serpente não peçonhenta, importante para o controle de roedores."},
        {"nome": "Mico-estrela", "descricao": "Pequeno primata com tufos brancos nas orelhas."},
        {"nome": "Tracajá", "descricao": "Quelônio que vive em rios e igarapés da região Amazônica."},
    ]

    for especie_data in especies_cesamar:
        especie_existente = Especie.query.filter_by(nome=especie_data["nome"], local_id=cesamar.id).first()
        if not especie_existente:
            nova_especie = Especie(
                nome=especie_data["nome"],
                descricao=especie_data["descricao"],
                local_id=cesamar.id
            )
            db.session.add(nova_especie)

    db.session.commit()
    print("Espécies associadas ao Parque Cesamar foram adicionadas com sucesso.")
