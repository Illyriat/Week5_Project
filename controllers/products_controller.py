from itertools import product
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.manufacture_controller import manufactures
from models.product import Product
from models.manufacture import Manufacture

import repositories.product_repository as product_repository
import repositories.manufacture_repository as manufacture_repository
import repositories.type_repository as type_repository

products_blueprint = Blueprint("product", __name__)

@products_blueprint.route("/")
def home():
    products = product_repository.select_all()
    return render_template("index.html", products = products)

# List of Products in the DB
@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)

# SHOW
# @products_blueprint.route("/products/<id>")
# def show(id):
#     product = product_repository.select(id)
#     manufactures = product_repository.manufactures(product)
#     return render_template("/products/show.html", product = product, manufactures = manufactures)

# NEW
@products_blueprint.route("/product/new", methods=['GET'])
def new_product():
    products = product_repository.select_all()
    manufactures = manufacture_repository.select_all()
    types = type_repository.select_all()
    return render_template("/products/new.html", products = products, manufactures = manufactures, types = types)


# CREATE
@products_blueprint.route("/products", methods=['POST'])
def create_product():
    manufacture_id = request.form['manufacture']
    type_id = request.form['type']
    model = request.form['model']
    description = request.form['description']
    stock_count = request.form['stock_count']
    trade_price = request.form['trade_price']
    sale_price = request.form['sale_price']
    manufacture = manufacture_repository.select(manufacture_id)
    type = type_repository.select(type_id)
    product = Product(model, description, stock_count, trade_price, sale_price, manufacture, type)
    product_repository.save(product)
    return redirect('/products')

# EDIT
@products_blueprint.route("/products/<id>/update", methods=['GET'])
def edit_products(id):
    product = product_repository.select(id)
    manufacture = manufacture_repository.select_all()
    return render_template('products/update.html', product = product, manufacture = manufacture)


# UPDATE
@products_blueprint.route("/products/<id>", methods=['POST'])
def update_products(id):
    manufacture_id = request.form['manufacture']
    type_id = request.form['type']
    model = request.form['model']
    description = request.form['description']
    stock_count = request.form['stock_count']
    trade_price = request.form['trade_price']
    sale_price = request.form['sale_price']
    manufacture = manufacture_repository.select(manufacture_id)
    type = type_repository.select(type_id)
    product = Product(model, description, stock_count, trade_price, sale_price, manufacture, type, id)
    product_repository.update(product)
    return redirect('/products/index.html')

# DELETE
@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')