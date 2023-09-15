from flask import render_template,redirect,flash
from flask_login import login_required
from app.productos import productos
import app
import os
from .forms import NewProductForm,EditProductForm

@productos.route('/create', methods=['GET','POST'])
def crear(): 
    p = app.models.Producto()
    form = NewProductForm()
    ## 
    if form.validate_on_submit():
        #guardar en base de datos
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        #subir en carpeat de imagenes 
        # campo imagen ( filestorage): 
        archivo= form.imagen.data
        archivo.save(os.path.abspath(os.getcwd()+"/app/productos/imagenes/"+p.imagen))
        flash("producto registrado correctamente")
        return redirect('/productos/listar')
    return render_template('new.html',
                           form=form)
          
@productos.route('/listar')
@login_required
def listar():
     ## seleccionar los profuctos
    productos = app.models.Producto.query.all() 
    return render_template("list.html", 
                            productos = productos)   
@productos.route('/editar/<producto_id>',methods=['GET','POST'])
@login_required
def editar (producto_id):
    p = app.models.Producto.query.get(producto_id)
    form = EditProductForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('producto actualizado')
        return redirect('/productos/listar')
    return render_template('new.html',
                           form=form)

@productos.route('/eliminar/<producto_id>')
@login_required
def eliminar (producto_id):
    p = app.models.Producto.query.get(producto_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('producto eliminado')
    return redirect('/productos/listar')

