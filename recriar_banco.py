import os
from app import create_app
from app.models import db

# Caminho do banco de dados
db_path = 'site.db'

# Remove o banco se já existir
if os.path.exists(db_path):
    print('Removendo banco de dados antigo...')
    os.remove(db_path)
else:
    print('Nenhum banco de dados antigo encontrado.')

# Cria o novo banco
app = create_app()
with app.app_context():
    db.create_all()
    print('Novo banco de dados criado com sucesso!')
