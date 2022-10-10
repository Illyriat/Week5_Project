from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.djequip import Djequip
from repositories.djequip_repository as djequip_repository

djequips_blueprint = Blueprint("djequip", __name__)

@djequips_blueprint.route("/djequip")
def mics():
    djequips = djequip_repository.select_all()
    return render_template("djequips/index.html", djequips = djequips)

@djequips_blueprint.route("/djequips/<id>")
def show(id):
    djequip = djequip_repository.select(id)
    manufactures = djequip_repository.manufactures(djequip)
    return render_template("/djequips/show.html", djequip = djequip, manufactures = manufactures)