from flask import Flask, render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
import json
with open("config.json") as c:
    params = json.load(c)["params"]
local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', params=params)







app.run(debug = True)

