from flask import render_template,redirect,flash
from flask_login import login_required
from app.clientes import clientes
import app

from .forms import ClienteForm,NewClienteForm,EditClienteForm


@clientes.route('/cliente', methods=['GET','POST'])
def crear(): 
    p = app.models.Cliente()
    form = NewClienteForm()
    c=p
    if form.validate_on_submit():
        #guardar en base de datos
        form.populate_obj(p)
        c.set_password(form.password.data)
        print(c)
        app.db.session.add(p)
        app.db.session.commit()  
        flash("cliente registrado correctamente")
        return redirect('/clientes/listar')
    return render_template('newCliente.html',
                           form=form)
    
@clientes.route('/listar')
@login_required
def listar():
     ## seleccionar los profuctos
    clientes= app.models.Cliente.query.all() 
    return render_template("listCliente.html", 
                            clientes = clientes)
       
@clientes.route('/editar/<cliente_id>',methods=['GET','POST'])
@login_required
def editar (cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    form = EditClienteForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('cliente actualizado')
        return redirect('/clientes/listar')
    return render_template('new.html',
                           form=form)    
    
 
 
@clientes.route('/eliminar/<cliente_id>')
@login_required
def eliminar (cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('cliente eliminado')
    return redirect('/clientes/listar')


    
    
    