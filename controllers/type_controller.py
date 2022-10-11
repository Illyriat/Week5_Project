from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.type import Type
import repositories.type_repository as type_repository

types_blueprint = Blueprint("type", __name__)

@types_blueprint.route("/type")
def types():
    types = type_repository.select_all()
    return render_template("types/index.html", types = types)

@types_blueprint.route("/types/<id>")
def show(id):
    type = type_repository.select(id)
    manufactures = type_repository.manufactures(type)
    return render_template("/types/show.html", type = type, manufactures = manufactures)