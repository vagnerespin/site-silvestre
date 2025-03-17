from app import create_app, db
from app.models import Usuario
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.create_all()

    # Verifica se já existe usuário admin
    if Usuario.query.filter_by(username="admin").first():
        print("Usuário admin já existe.")
    else:
        senha_hash = generate_password_hash("admin123")
        admin = Usuario(username="admin", password=senha_hash, is_admin=True)
        db.session.add(admin)
        db.session.commit()
        print("Usuário admin criado com sucesso. Login: admin | Senha: admin123")
