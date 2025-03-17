@echo off
setlocal EnableDelayedExpansion

:: Caminho das pastas
set "FONTE=portal_mapa_palmas_autenticacao"
set "DESTINO=portal_mapa_palmas"
set "BACKUP=backup_portal_mapa_palmas_%DATE:/=-%_%TIME::=-%.bak"

echo ===============================================
echo INICIANDO SINCRONIZAÇÃO DO PROJETO PORTAL PALMAS
echo ===============================================

:: Criar backup da pasta destino
echo Criando backup da pasta destino...
mkdir "!BACKUP!"
xcopy /Y /E /I "%DESTINO%" "!BACKUP!" > nul
echo Backup salvo em: !BACKUP!

:: Copiar arquivos atualizados
echo.
echo Copiando arquivos atualizados...
xcopy /Y /S /I "%FONTE%\app" "%DESTINO%\app"
xcopy /Y /I "%FONTE%\run.py" "%DESTINO%\run.py"

echo.
echo Sincronização finalizada com sucesso!

echo.
echo Pressione qualquer tecla para sair...
pause > nul