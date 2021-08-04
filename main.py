from pymongo import MongoClient
import pandas as pd
from flask import Flask, request, redirect,jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app, support_credentials=True)
#settings
app.secret_key = "mysecretkey"
client = MongoClient("mongodb+srv://probeapk:1718123563@cluster0.ydel3.mongodb.net/<>?retryWrites=true&w=majority")
db = client.probeapk

def cargarData(datos):
	collection = db.encuestas
	dato=json.loads(datos)
	collection.insert_one(dato)

def buscarUsuario(cedula,password):
	collection=db.usuarios
	role=collection.find_one({"cedula":cedula,"password":password})
	if(role!=None):
		return role['nombre'],role['apellido'],role['role']
	else:
		role="null"
		return role

def contarTrabajo(cedula,fecha):
	collection=db.encuestas
	x=collection.find({'cedEnc':cedula,'fecha':fecha})
	x=list(x)
	x=len(x)
	return x


@app.route('/query-example', methods=["POST"])
@cross_origin(supports_credentials=True)
def query_example():
    # if key doesn't exist, returns None
    cargarData((request.data).decode('utf-8'))
    return 'exitoso'

@app.route('/obtenerRol', methods=["Get"])
@cross_origin(supports_credentials=True)
def obtenerRol():
    # if key doesn't exist, returns None
	cedula = request.args.get('cedula')
	password = request.args.get('password')
	nombre,apellid,role=buscarUsuario(cedula,password)
	print(role)
	return jsonify({'nombre':nombre,'apellido':apellid,'role':role})

@app.route('/obtenerTotTrab', methods=["Get"])
@cross_origin(supports_credentials=True)
def obtenerTotTrab():
    # if key doesn't exist, returns None
	cedula = request.args.get('cedula')
	fecha = request.args.get('fecha')
	total=contarTrabajo(cedula,fecha)
	print(total)
	return jsonify({'total':total})


app.run('0.0.0.0',8080)
