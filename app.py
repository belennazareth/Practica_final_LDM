from flask import Flask, render_template, abort, redirect
import os

app = Flask(__name__)

films = ()	

@app.route('/')
def inicio():
    return render_template("base.html",films=films)

@app.route('/base')
def biblioteca():
    return render_template("base.html", films=films)

@app.route('/error')
def error():
    return abort(404)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=True)