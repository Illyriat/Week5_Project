from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.manufacture_repository as manufacture_repository
import repositories.product_repository as product_repository
import repositories.type_repository as type_repository

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