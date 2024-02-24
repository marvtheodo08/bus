from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def homepage():
  if request.method == "POST":  
  return render_template("index.html")

                         
