from flask_login import login_user,current_user ,logout_user
from flask import render_template,redirect,flash
from flask_login import login_required
from app.auth import auth 
from .forms import Loginform
import app

@auth.route('/login',
            methods=['GET', 'POST'])
def login():
    form = Loginform()   
    if form.validate_on_submit():
        #se selecciona al ususario por username
        c= app.models.Cliente.query.filter_by(username = form.username.data).first()
        if c is None or not  c.check_password(form.password.data):
         #flash
            flash('usuario o contraseña incorrectos')
            return redirect ('/auth/login') 
        else:
            login_user(c,remember=True)
            flash('sesión iniciada con exito')
            return redirect('/productos/listar')
    return render_template('login.html',
                           form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('sesión cerrada con exito')
    return redirect ('/auth/login')