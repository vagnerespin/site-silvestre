@echo off
echo ===============================================
echo RESTAURAR BACKUP - PROJETO PORTAL PALMAS
echo ===============================================

set "DESTINO=portal_mapa_palmas"

:: Listar últimas pastas de backup
echo Buscando backups disponíveis...
for /d %%i in (backup_portal_mapa_palmas_*) do echo %%i

set /p BACKUPDIR=Digite o nome exato da pasta de backup que deseja restaurar:

echo Restaurando arquivos...
xcopy /Y /S /I "%BACKUPDIR%\*" "%DESTINO%\"

echo Restauração concluída com sucesso!
pause