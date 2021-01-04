from flask import render_template, url_for, redirect, request

from . import modulo1_bp

from ejecutar import conn

from flask_login import current_user

class Persona:
    
    nombre = ""
    apellido = ""
    
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


@modulo1_bp.route('/modulo1/contacto')
def contacto():
    
    if current_user.is_authenticated:
        return 'El loco esta conectado'
    
    p1 = Persona("Raul","Ruz")
    errores = ["sadfkjasdfhkjas"]
    print(url_for('modulo1.contacto'))
    return render_template("contacto/contacto.html", persona = p1, errores= errores)


