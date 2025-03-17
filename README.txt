
==============================
PORTAL DA FAUNA - FLASK APP
==============================

Este projeto é um sistema web com Flask, com funcionalidades de:
✅ Cadastro de usuários
✅ Login e logout
✅ Cadastro de espécies associadas a locais
✅ Exibição de mapa interativo com Leaflet
✅ Popup com mascotes e modais de detalhes por marcador

-----------------------------------
1. COMO EXECUTAR O PROJETO:
-----------------------------------

1.1 Extraia o conteúdo do ZIP em uma pasta local:
Exemplo: C:\Users\SeuUsuario\Desktop\site_silvestres

1.2 No terminal, vá até essa pasta:
> cd C:\Users\SeuUsuario\Desktop\site_silvestres

1.3 Crie e ative o ambiente virtual:
> python -m venv venv
> venv\Scripts\activate     (Windows)

1.4 Instale os pacotes necessários:
> pip install flask flask_sqlalchemy flask_login

1.5 Inicialize o banco de dados (primeira vez):
> python
>>> from app import create_app
>>> from app.models import db
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
>>> exit()

1.6 Rode o sistema:
> python run.py

1.7 Acesse no navegador:
http://127.0.0.1:5000

-----------------------------------
2. ORGANIZAÇÃO DAS PASTAS:
-----------------------------------
site_silvestres/
├── app/
│   ├── __init__.py          → inicia a aplicação Flask
│   ├── models.py            → classes Usuario, Local, Especie
│   ├── views.py             → rotas de espécies e locais
│   └── auth.py              → rotas de login/logout/cadastro
├── templates/
│   ├── base.html            → layout base com menu dinâmico
│   ├── index.html           → mapa com popup e modais
│   ├── listar_especies.html
│   ├── cadastro_especie.html
│   ├── login.html
│   └── cadastro_usuario.html
├── static/
│   └── img/                 → adicione aqui: mascote_mucura.png, mascote_capivara.png, mascote_arara.png
└── run.py                  → arquivo principal para iniciar o servidor

-----------------------------------
3. CONTATO E SUPORTE
-----------------------------------
Caso precise de ajuda, você pode reexecutar este projeto a qualquer momento ou ajustar os arquivos com base neste guia técnico.

Bom desenvolvimento! 🐾💻
