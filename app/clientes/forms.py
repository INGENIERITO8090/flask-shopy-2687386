from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,StringField,EmailField
from wtforms.validators import InputRequired,NumberRange,Email,Length
from flask_wtf.file import FileField , FileRequired,FileAllowed


class ClienteForm():    
    username =  StringField("Ingrese nombre cliente",validators=[InputRequired(message='Nombre requerido')])
    email =  EmailField("Ingrese email",validators=[InputRequired(message="CAMPO REQUERIDO "),
                                                    Email(message="se necesita una direccion con @")])
    password =  StringField("Ingrese contraseña",validators=[InputRequired(message='Contraseña'),Length(10,10)]) 
    
class NewClienteForm(FlaskForm,ClienteForm):
   
    submit = SubmitField("Guardar") 
      
      
class EditClienteForm(FlaskForm,
                          ClienteForm):
    submit= SubmitField("Actualizar")
