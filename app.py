from flask import Flask, request, render_template, session, redirect
import pymysql
import os

app = Flask(__name__)
app.secret_key = os.urandom(64)

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

@app.route('/ventas')
def ventas():
	return render_template('ventas.html')

@app.route('/inicio')
def inicio():
	return render_template('inicio.html')

@app.route('/salir')
def salir():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')