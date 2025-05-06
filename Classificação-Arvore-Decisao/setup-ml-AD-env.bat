@echo off
echo Criando ambiente virtual com Pipenv...

REM Caminho para seu requirements.txt
set REQUIREMENTS=C:\Users\dccas\config\dev-ml-AD\requirements.txt

REM Instala as dependências no novo ambiente pipenv
pipenv install -r %REQUIREMENTS%

echo Ambiente criado com sucesso!
echo Abrindo terminal com ambiente ativado...

REM Abre o cmd com o ambiente já ativado
start cmd /k "pipenv shell"
