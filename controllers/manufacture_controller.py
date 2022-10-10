from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacture import Manufacture
from repositories.manufacture_repository import *
from repositories.desk_repository import *
from repositories.mic_repository import *
from repositories.djequip_repository import *

manufactures_blueprint = Blueprint("manufacture", __name__)

@manufactures_blueprint.route("/manufacture")
def manufactures():
    manufactures = manufactrue_repository.select_all()
    return render_template("manufactures/index.html", manufactures = manufactures)

@manufactures_blueprint.route("/manufactures/<id>")
def show(id):
    manufacture = manufacture_repository.select(id)
    mics = mic_repository.manufactures(mic)
    desks = desk_repository.manfactures(desk)
    djequips = djequip_repository.manufactures(djequip)
    return render_template("/manufactures/show.html", manufactures = manufactures, mic = mic, desk = desk, djequip = djequip)