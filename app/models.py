from app import db
from datetime  import datetime

#modelos -entidades de el proyeto 
class Cliente(db.Model):
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key = True)      #para tener el dato como entero se usa el db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))  #para decir que un dato es unico se usa el unique =true y para llaves primarias se usa el primary_key
    password = db.Column(db.String(200))
    email = db.Column(db.String(100),unique=True)

class Producto(db.Model):
    __tablename__="productos"
    id = db.Column(db.Integer,
                    primary_key = True)      #para tener el dato como entero se usa el db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120),
                         unique=True)  #para decir que un dato es unico se usa el unique =true y para llaves primarias se usa el primary_key
    precio = db.Column(db.Numeric(precision=10,
                         scale = 2))
    imagen = db.Column(db.String(120))
    
class Venta(db.Model):
    __tablename__="ventas"
    id = db.Column(db.Integer,
                    primary_key = True)
    fecha = db.Column(db.DateTime ,
                       default = datetime.utcnow ) #Se coloca para que la fecha sea default asi y se coloque la que esta en el sistema 
    cliente_id = db.Column(db.Integer,
                        db.ForeignKey('clientes.id'))

class Detalle(db.Model):
    __tablename__="detalles"
    id = db.Column(db.Integer,
                    primary_key = True)
    producto_id = db.Column(db.Integer,
                          db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer,
                          db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)