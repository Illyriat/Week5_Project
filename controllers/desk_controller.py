from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.desk import Desk
from repositories.desk_repository import desk_repository

desks_blueprint = Blueprint("desk", __name__)

@desks_blueprint.route("/desks")
def desks():
    desks = desk_repository.select_all()
    return render_template("desks/index.html", desks = desks)

@desks_blueprint.route("/desks/<id>")
def show(id):
    desk = desk_repository.select(id)
    manufactures = desk_repository.manufactures(desk)
    return render_template("/desks/show.html", desk = desk, manufactures = manufactures)