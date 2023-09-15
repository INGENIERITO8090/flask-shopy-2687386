from flask import Flask,render_template 
from flask_login import LoginManager
from .config import Config
from flask_migrate import Migrate, migrate 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .mi_blueprint import mi_blueprint
from app.productos import productos 
from app.clientes import clientes
from flask_bootstrap import  Bootstrap 
from app.auth import auth   


#INICIALIZAR EL OBJETO FLASK
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view= "/auth/login"

#inicializar el onjeto sqlAlchemy
db=SQLAlchemy(app)  #tops de datos : string number etc...
migrate=Migrate(app,db) 


#registrar modulos(blueprints)
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos) 
app.register_blueprint(clientes)
app.register_blueprint(auth)




from .models import Cliente,Venta,Producto,Detalle  

@app.route('/prueba')
def prueba():
    return render_template('base.html')