from . import autenticacion_bp

from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user

from ejecutar import conn
from Usuario import Usuario

@autenticacion_bp.route('/iniciar_sesion', methods = ["POST","GET"])
def iniciar_sesion():
    errores = []
    
    if current_user.is_authenticated:
        print("El usuario ya esta dentro del sistema")
        return redirect(url_for("index3"))
    else:
        print("El usuario no esta dentro del sistema")
        
        if request.method == "POST":
            
            rut = request.form["rut"]
            
                     
            cur = conn.cursor()
            cur.execute('SELECT RUT FROM CLIENTE WHERE RUT = :RUT',[rut])
            res = cur.fetchone()
            
            if res == None:
                errores.append("Usuario no existente o invalido")
            else:
                login_user(Usuario(res[0]))
                print("Usuario ingreso")
                return redirect(url_for('index3'))
        
    
    return render_template("autenticacion/iniciar_sesion.html", errores=errores)


@autenticacion_bp.route("/cerrar_sesion")
def cerrar_sesion():
    
    if current_user.is_authenticated:
        logout_user()
        print("Usuario salio")
    return redirect(url_for("index2"))