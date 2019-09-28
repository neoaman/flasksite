import random
from flask import Flask, render_template,request,session,redirect,Response
from flask_sqlalchemy import SQLAlchemy
import os
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import json

# 'mysql://username:password@localhost/db_name'
with open("config.json") as c:
    params = json.load(c)["params"]
local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'

path = "D:\\STUDY PROCESS\\Flask\\flasksite\\static\\dataset\\"
image = "D:\\STUDY PROCESS\\Flask\\flasksite\\static\\img\\"
dataset = os.listdir("D:\\STUDY PROCESS\\Flask\\flasksite\\static\\dataset")


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Amanneo:P@ssw0rd@Amanneo.mysql.pythonanywhere-services.com/Amanneo$neonature'
#db = SQLAlchemy(app)
#db = DAL('mysql://<your_username>:<your_mysql_password>@<your_mysql_hostname>/<your_database_name>')
"""
class Contact(db.Model):
    name = db.Column(db.String(20), nullable=False, primary_key =True )
    email = db.Column(db.String(30), nullable=False)
    subject = db.Column(db.String(50), nullable=True)
    message = db.Column(db.String(100), nullable=False)
"""

@app.route("/")
def home():
    return render_template('index.html', params=params)

@app.route('/test')
def chartTest():
  df = pd.read_csv(path+dataset[1])
  df.price.plot()

  plt.savefig(image+"plot1.png")
  return render_template('plot.html', url ="/static/img/plot1.png")

app.run(debug = True)

