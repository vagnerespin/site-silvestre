
from app import db, create_app
from app.models import Local
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

app = create_app()

with app.app_context():
    try:
        db.create_all()
        print("✔ Tabelas verificadas/criadas com sucesso.")

        with db.session.connection() as conn:
            result = conn.execute(text("PRAGMA table_info(local);"))
            colunas = [row[1] for row in result.fetchall()]

            if "latitude" not in colunas:
                conn.execute(text("ALTER TABLE local ADD COLUMN latitude FLOAT;"))
                print("✔ Campo 'latitude' adicionado à tabela 'local'.")
            else:
                print("✔ Campo 'latitude' já existe.")

            if "longitude" not in colunas:
                conn.execute(text("ALTER TABLE local ADD COLUMN longitude FLOAT;"))
                print("✔ Campo 'longitude' adicionado à tabela 'local'.")
            else:
                print("✔ Campo 'longitude' já existe.")

        parque = Local.query.filter_by(nome="Parque Cesamar").first()
        if not parque:
            parque = Local(
                nome="Parque Cesamar",
                descricao="Local com rica fauna de espécies silvestres",
                latitude=-10.209744,
                longitude=-48.324348
            )
            db.session.add(parque)
            db.session.commit()
            print("✔ Parque Cesamar inserido com sucesso.")
        else:
            print("✔ Parque Cesamar já está cadastrado.")

    except OperationalError as e:
        print("❌ Erro de operação no banco de dados:", e)
    except Exception as e:
        print("❌ Erro geral:", e)
