from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,StringField,EmailField,PasswordField
from wtforms.validators import InputRequired,NumberRange,Email,Length

class Loginform(FlaskForm):
    username=StringField(label="nombre de usuario")
    password=PasswordField(label=" Clave")
    submit = SubmitField(label="Iniciar sesion")
    