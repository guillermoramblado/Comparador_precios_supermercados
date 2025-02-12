from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#creamos la aplicacion de Flask

app = Flask(__name__)
#aplico las configuraciones tras crear mi aplicacion Flask
app.config.from_object(Config)
#instanciamos la base de datos y la herramienta que me permite agregar migraciones
db = SQLAlchemy(app)
migrate= Migrate(app,db)

#Este __init__ permitirá ver el directorio app como un paquete Python
#Mediante el siguiente 'import' indicaremos los elementos del paquete 'app' que se expondrá al exterior
from app import routes, models
from app import db