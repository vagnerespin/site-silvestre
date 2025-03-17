from app import create_app, db

# Cria o app e ativa o contexto
app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Banco de dados criado com sucesso!")