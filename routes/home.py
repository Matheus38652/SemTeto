from flask import Blueprint, render_template

home = Blueprint(name='home')

@home.route
def home():
    return render_template('index.html')
    ...