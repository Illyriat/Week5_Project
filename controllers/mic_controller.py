from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.mic import Mic
from repositories.mic_repository import mic_repository

mics_blueprint = Blueprint("mic", __name__)

@mics_blueprint.route("/mic")
def mics():
    mics = mic_repository.select_all()
    return render_template("mics/index.html", mics = mics)

@mics_blueprint.route("/mics/<id>")
def show(id):
    mic = mic_repository.select(id)
    manufactures = mic_repository.manufactures(mic)
    return render_template("/mics/show.html", mic = mic, manufactures = manufactures)