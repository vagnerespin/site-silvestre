from app import create_app
from app.models import db, Usuario

app = create_app()
with app.app_context():
    admin = Usuario.query.filter_by(email='admin@admin.com').first()
    if not admin:
        admin = Usuario(email='admin@admin.com', senha='admin123')
        db.session.add(admin)
        db.session.commit()
        print('Usuário admin criado com sucesso!')
    else:
        print('Usuário admin já existe.')
