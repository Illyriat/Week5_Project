from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacture import Manufacture

import repositories.manufacture_repository as manufacture_repository
import repositories.product_repository as product_repository
import repositories.type_repository as type_repository

manufactures_blueprint = Blueprint("manufacture", __name__)

@manufactures_blueprint.route("/")
def home():
    manufacture = manufacture_repository.select_all()
    return render_template("index.html", manufacture = manufacture)

# List of Manufactures
@manufactures_blueprint.route("/manufacture")
def manufactures():
    manufactures = manufacture_repository.select_all()
    return render_template("manufacture/index.html", manufactures = manufactures)


# SHOW
# @manufactures_blueprint.route("/manufactures/<id>")
# def show(id):
#     manufactures = manufacture_repository.select(id)
#     products = product_repository.manufactures(products)
#     types = type_repository.manfactures(types)
#     return render_template("/manufactures/show.html", manufactures = manufactures, type = types, product = products)


# NEW
@manufactures_blueprint.route("/manufacture/new", methods=['GET'])
def new_manufacture():
    manufactures = manufacture_repository.select_all()
    return render_template("/manufacture/new.html", manufactures = manufactures)


# CREATE
@manufactures_blueprint.route("/manufacture", methods=['POST'])
def create_manufacture():
    name = request.form['name']
    manufacture = Manufacture(name)
    manufacture_repository.save(manufacture)
    return redirect('/manufacture')


# DELETE
@manufactures_blueprint.route("/manufacture/<id>/delete", methods=['POST'])
def delete_manufacture(id):
    manufacture_repository.delete(id)
    return redirect('/manufacture')