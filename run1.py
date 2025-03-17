from app import create_app, db
from app.models import Local, Especie, Usuario
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.create_all()

    if not Local.query.first():
        cesamar = Local(nome='Parque Cesamar')
        db.session.add(cesamar)
        db.session.commit()

        especies = [
            Especie(nome_comum='Capivara', nome_cientifico='Hydrochoerus hydrochaeris', descricao='Mamífero roedor aquático.', local_id=cesamar.id),
            Especie(nome_comum='Socozinho', nome_cientifico='Butorides striata', descricao='Ave pescadora.', local_id=cesamar.id),
            Especie(nome_comum='Tatu-galinha', nome_cientifico='Dasypus novemcinctus', descricao='Mamífero cavador noturno.', local_id=cesamar.id)
        ]
        db.session.bulk_save_objects(especies)

        admin = User(username='admin', password=generate_password_hash('1234'))
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
