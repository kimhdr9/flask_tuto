from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template("public/index.html")

@app.route('/about/')
def about():
    return " au sujet du site "

@app.route('/exemples/')
def exemples():
    return "exemple"