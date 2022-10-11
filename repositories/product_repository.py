from itertools import product
from db.run_sql import run_sql

from models.product import Product
from models.type import Type
from models.manufacture import Manufacture

import repositories.type_repository as type_repository
import repositories.manufacture_repository as manufacture_repository


def save(product):
    sql = "INSERT INTO products(model, description, stock_count, trade_price, sale_price, manufacture_id, type_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.model, product.description, product.stock_count, product.trade_price, product.sale_price, product.manufacture.id, product.type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        manufacture = manufacture_repository.select(row['manufacture_id'])
        type = type_repository.select(row['type_id'])
        product = Product(row['model'], row['description'], row['stock_count'], row['trade_price'], row['sale_price'], manufacture, type, row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        product = Product(result['model'], result['description'], result['stock_count'], result['trade_price'], result['sale_price'], manufacture['id'], type['id'], result['id'])
    return product

def manufacture():
    sql = "SELECT * FROM manufactures WHERE id = %s"
    values = [product.manufacture.id]
    results = run_sql(sql, values)[0]
    product = Product(results['model'], results['id'])
    return manufacture

def delete_all():
    sql = "DELETE FROM manufactures"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)