from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    return render_template('index.html')