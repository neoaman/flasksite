import random
from flask import Flask, render_template,request,session,redirect,Response
from flask_sqlalchemy import SQLAlchemy
import os
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import json

# 'mysql://username:password@localhost/db_name'
with open("/home/Amanneo/neo/config.json") as c:
    params = json.load(c)["params"]
local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'

path = "/home/Amanneo/neo/flasksite/static/dataset/"
image = "/home/Amanneo/neo/flasksite/static/img/"
dataset = os.listdir("/home/Amanneo/neo/flasksite/static/dataset")


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

@app.route("/",methods=['GET','POST'])
def home():
    if (request.method == "POST"):
            cname = request.form.get('name')
            cemail = request.form.get('email')
            csub = request.form.get('subject')
            cmes = request.form.get('message').replace(",", "_")

            with open("/home/Amanneo/neo/contact.csv", mode='a') as file_:
                file_.write("{},{},{},{}".format(cname, cemail,csub,cmes))
                file_.write("\n")

    return render_template('index.html', params=params)

@app.route('/test')
def chartTest():
      df = pd.read_csv(path+dataset[1])
      df.price.plot()
      plt.savefig(image+"plot1.png")
      return render_template('plot.html', url ="/static/img/plot1.png")

@app.route('/dashboard',methods=['GET','POST'] )
def dashboard():
    datasets = os.listdir("D:\\STUDY PROCESS\\Flask\\flasksite\\static\\dataset\\")
    contacts = pd.read_csv("/home/Amanneo/neo/contact.csv");
    detail = list(contacts.values)

    if ('user' in session and session['user'] == params['admin_user']):
        return render_template('dashboard.html', params=params,detail=detail,datasets=datasets)
    if request.method == 'POST':
        passs = request.form.get('password')
        uname = request.form.get('username')
        if (uname == params['admin_user'] and passs == params['admin_pass']):
            session['user'] = uname
            return render_template('dashboard.html', params=params,detail=detail, datasets=datasets)
        else:
            return render_template('login.html', params=params)
    return render_template('login.html', params=params)

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')






