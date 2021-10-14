## Api-repuestos-mongo
Mini ApiRest con FastApi y MongoDB

## Comando Para Crear requeriments.txt

pip freeze > requeriments.txt

## Comando Para Activar o Instalar los paquetes en requeriments.txt

pip install -r requeriments.txt

## Instalación De FastApi

pip install fastapi

## También vas a necesitar un servidor ASGI para producción cómo Uvicorn

pip install uvicorn[standard]

## Corre el servidor con:

uvicorn main:app --reload
