from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
from models.manufacture import Manufacture
from repositories.type_repository import type_repository
from repositories.product_repository import product

products_blueprint = Blueprint("product", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)

@products_blueprint.route("/products/<id>")
def show(id):
    product = product_repository.select(id)
    manufactures = product_repository.manufactures(product)
    return render_template("/products/show.html", product = product, manufactures = manufactures)