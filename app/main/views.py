from flask import render_template
from . import main


@main.route("/")
def homepage():
    return render_template("home/index.html", title="Bem vindo!")
    