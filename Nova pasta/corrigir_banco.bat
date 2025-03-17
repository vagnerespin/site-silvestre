
@echo off
echo ==================================
echo ATIVANDO AMBIENTE VIRTUAL...
call venv\Scripts\activate

echo ==================================
echo EXECUTANDO CORREÇÕES NO BANCO...
python setup_banco_completo_corrigido.py

echo ==================================
echo FINALIZADO. Pressione qualquer tecla para sair...
pause
