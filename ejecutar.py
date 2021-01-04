import cx_Oracle
#cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\instantclient_19_9")

from flask import Flask
from flask import render_template, url_for, redirect, request
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from Usuario import Usuario


app = Flask(__name__)
Bootstrap(app)

## Configuracion

#BD_USUARIO ="Tarea_3"
#BD_PASSWORD ="1234"
#BD_SERVICIO ="localhost:1521/XE"

BD_USUARIO ="Proyecto_final"
BD_PASSWORD ="1234"
BD_SERVICIO ="localhost:1521/XE"

conn = cx_Oracle.connect(BD_USUARIO, BD_PASSWORD, BD_SERVICIO)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(rut):
    cur = conn.cursor()
    cur.execute('SELECT RUT FROM CLIENTE WHERE RUT = :RUT',[rut])
    res = cur.fetchone()
    
    if (res == None):
        return None
    else:
        return Usuario(res[0])
    

from publico import publico_bp
app.register_blueprint(publico_bp)

from modulo1 import modulo1_bp
app.register_blueprint(modulo1_bp)

from autenticacion import autenticacion_bp
app.register_blueprint(autenticacion_bp)

app.config["SECRET_KEY"] = '234lfkj345;lg46;[78]'



## RUTAS

@app.route('/')
def inicio():
    errores = ["El archivo solicitado es incorrecto"]
    return render_template("index.html", errores = errores)


@app.route('/nueva') #nueva template de prueba
def nueva():
    
    return render_template("nueva.html")

@app.route('/lista_clientes')
def lista_clientes():

    cur = conn.cursor()
    cur.execute('SELECT * FROM CLIENTE')
    #rows = cur.fetchone()
    rows = cur.fetchall()
    cur.close()
    #print(rows)
    return render_template('lista_clientes.html', filas=rows)
    

@app.route('/lista_yates')
def lista_yates():

    cur = conn.cursor()
    cur.execute('SELECT * FROM EMBARCACION')

    #rows = cur.fetchone()
    rows = cur.fetchall()
    cur.close()
    #print(rows)
    return render_template('lista_yates.html', filas=rows)

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')

@app.route('/test')
def test():
    return render_template('test_1.html')

@app.route('/actualizar_cliente', methods = ['GET','POST'])
def actualizar_cliente():
    cur = conn.cursor()
    cur.execute('SELECT * FROM CLIENTE')
    #rows = cur.fetchone()
    rows = cur.fetchall()
    cur.close()
    #print(rows)

    mensaje = ""
    salida = ""

    if request.method == 'GET':
        rut = request.args.get("rut")
        nombre = request.args.get("nombre")

        
    elif request.method == 'POST':
        
        rut = request.form["rut"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        correo = request.form["correo"]
        nacionalidad = request.form["nacionalidad"]
        password = request.form["password"]
              
        cursor = conn.cursor()
        mensaje,salida = cursor.var(str),cursor.var(str)
                
        cursor.execute('CALL ACTUALIZAR_CLIENTE(:RUT,:NOMBRE,:APELLIDO,:CORREO,:NACIONALIDAD,:PASSWORD,:MENSAJE,:SALIDA)',[rut,nombre,apellido,correo,nacionalidad,password,mensaje,salida])

        conn.commit()
        cursor.close()
        
    else:
        return '<h1> Metodo no encontrado </h1>'
    
    return render_template('actualizar_cliente.html', mensaje=mensaje, salida=salida)


@app.route('/new_cliente', methods = ['GET','POST'])
def new_cliente():

    mensaje = ""
    salida = ""

    if request.method == 'GET':
        rut = request.args.get("rut")       
        
    elif request.method == 'POST':
        
        rut = request.form["rut"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        correo = request.form["correo"]
        nacionalidad = request.form["nacionalidad"]
        password = request.form["password"]
              
        cursor = conn.cursor()

        mensaje,salida = cursor.var(str),cursor.var(str)
                
        cursor.execute('CALL NUEVO_CLIENTE(:RUT,:NOMBRE,:APELLIDO,:CORREO,:NACIONALIDAD,:PASSWORD,:MENSAJE,:SALIDA)',[rut,nombre,apellido,correo,nacionalidad,password,mensaje,salida])

        conn.commit()
        cursor.close()
        
    else:
        return '<h1> Metodo no encontrado </h1>'
    
    return render_template('new_cliente.html', mensaje=mensaje, salida=salida)

    
@app.route('/login')
def login():
    
    return render_template('login_cliente_no.html')

@app.route('/vitrina')
def vitrina():
    
    return render_template('base2.html')
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1011, debug=True)


