# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 16:39:40 2021

@author: kchan
"""

import pymongo
import pandas as pd
from flask import Flask, request, redirect
import json
app = Flask(__name__)
#settings
app.secret_key = "mysecretkey"
client = pymongo.MongoClient("mongodb+srv://probeapk:1718123563@cluster0.ydel3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.probeapk
collection = db.usuarios

def cargarData(datos):
    dato=json.loads(datos)
    collection.insert_one(dato)
          

def consultartrabajo():  
    #collection.insert_one({"cedulaEncuestador": "1718121111","cedulaSupervisor": "1718123563","fecha":"03/08/2021"})
    data = pd.DataFrame(list(collection.find()))

@app.route('/', methods=["GET","POST"])
def Index():
    if request.method == 'POST':
       pass
 
@app.route('/query-example', methods=["POST"])
def query_example():
    # if key doesn't exist, returns None
    cargarData((request.data).decode('utf-8'))
    return 'exitoso'
    


if __name__ == "__main__":
	app.run(host='0.0.0.0',port = 8080)

    



