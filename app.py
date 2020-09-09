from flask import Flask, request, render_template, session, redirect, jsonify
import pymysql
import os
from flask_cors import CORS
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(64)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/inventario')
def inventario():
	return render_template('inventario.html')

@app.route('/tasa')
def tasa():
	return render_template('tasa.html')

@app.route('/productos')
def productos():
	return render_template('productos.html')

@app.route('/productosv', methods = ['POST'])
def productosv():
	datos = request.get_json()
	conexion = pymysql.connect('localhost', 'root', '', 'inventarioapp')
	cursor = conexion.cursor()
	print(datos)
	app.config['UPLOAD_FOLDER'] = './static/productos'
	imagen = None
	archivo = None
	if 'file' in request.files:
		imagen = request.files['file']
	if imagen.filename == '':
		archivo = 'Nada'
	archivo = secure_filename(imagen.filename)
	ruta = './static/productos/'+ archivo
	sql = "INSERT INTO inventario() VALUES (%s, %s, %s, %s, %s, %s)"
	cursor.execute(sql, (datos['codigo'], datos['nombre'], datos['descripcion'], datos['cantidad'], datos['precio'], archivo))
	conexion.commit()
	conexion.close()
	return jsonify('Producto registrado satisfactoriamente')

@app.route('/ventas')
def ventas():
	return render_template('ventas.html')

@app.route('/inicio')
def inicio():
	return render_template('inicio.html')

@app.route('/salir')
def salir():
	return render_template('index.html')

@app.route('/tasav', methods = ['POST'])
def tasav():
	valor = request.get_json()['valor']
	fecha = datetime.now().date()
	print(valor, fecha)
	return jsonify(valor)

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')