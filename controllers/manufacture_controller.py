from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories.manufacture_repository import *
from repositories.product_repository import *
from repositories.type_repository import *

manufactures_blueprint = Blueprint("manufacture", __name__)

@manufactures_blueprint.route("/manufacture")
def manufactures():
    manufactures = manufacture_repository.select_all()
    return render_template("manufactures/index.html", manufactures = manufactures)

@manufactures_blueprint.route("/manufactures/<id>")
def show(id):
    manufactures = manufacture_repository.select(id)
    products = product_repository.manufactures(products)
    types = type_repository.manfactures(types)
    return render_template("/manufactures/show.html", manufactures = manufactures, type = types, product = products)