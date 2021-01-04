from flask import render_template, url_for, redirect, request

from . import publico_bp

from ejecutar import conn


@publico_bp.route('/lista_clientes')
def lista_clientes():
    
    cur = conn.cursor()
    cur.execute('SELECT * FROM CLIENTE')
    rows = cur.fetchall()
    cur.close()
    return render_template('lista_clientes.html', filas=rows)