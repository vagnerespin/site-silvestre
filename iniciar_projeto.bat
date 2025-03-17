
@echo off
echo ==================================
echo REMOVENDO BANCO ANTIGO (site.db)...
del site.db

echo ==================================
echo ATIVANDO AMBIENTE VIRTUAL...
call venv\Scripts\activate

echo ==================================
echo EXECUTANDO SETUP DO BANCO...
python setup_banco_completo_corrigido.py

echo ==================================
echo INICIANDO SERVIDOR FLASK...
python run.py
