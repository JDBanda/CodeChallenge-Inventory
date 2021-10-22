# Desafio de código - Inventario 
En este repositorio se puede encontrar el código base para clonar la API del inventario.

## Generalidades
Se han incluido dos archivos adicionales para que la clonación se realice sin problemas.
- **Archivo de mixtures:** Es básicamente el archivo de base de datos pero formateado de manera que al correr unos comandos podamos importar los datos a BD.
- **Archivo de requerimientos:** Para que no haga falta ningun paquete en el entorno de Python

## Como usar
- Clonar el proyecto con `git clone <url>`
- Crea un entorno virtual, no importa con que herramienta mientras la versión de python sea al menos 3.7
- Una vez dentro del entorno virtual será necesario copiar los requerimientos `pip install -r requirements.txt`
- Ejecutar las migraciones `python manage.py migrate`
- Copiar los mixtures para tener datos de prueba `python manage.py loaddata fixture.json`
- Verificar las credenciales de BD de acuerdo a las que tenga localmente en el archivo CodeChallengeInventory/setting.py
- Finalmente se podrá correr el servidor con `python manage.py runserver`

## Postman
- [Documentación de la API](https://documenter.getpostman.com/view/13042173/UV5ZDHh5)
- [Entorno y colección de API](https://www.postman.com/JDBanda/workspace/code-challenge-inventory/overview)

# CodeChallenge - Inventory 
En este repositorio se puede encontrar el código base para clonar la API del inventario.

## General information
It has been included two extra files to reduce clonning operation problems.
- **Mixtures file:** It is basically the db.json file but formatted to be imported with django into database records.
- **Requirements file:** Python packages to install.

## How to use it
- Clone the repo with `git clone <url>`
- Create a virtual environment, no matter the tool the important part is to use python 3.7 at least
- When you are into the virtual environment it will be nessesary to copy the requirements `pip install -r requirements.txt`
- Then execute migrations `python manage.py migrate`
- Copy the mixture for testing data `python manage.py loaddata fixture.json`
- Verify the DB credentials in the file CodeChallengeInventory/setting.py for your local instance
- Finally you could run the server with `python manage.py runserver`

## Postman
- [API Documentation](https://documenter.getpostman.com/view/13042173/UV5ZDHh5)
- [API Environment and collection](https://www.postman.com/JDBanda/workspace/code-challenge-inventory/overview)
