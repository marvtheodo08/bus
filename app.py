from flask import Flask, render_template, request
import sqlite3

@app.route('/', methods=['POST'])
def homepage():
                         
