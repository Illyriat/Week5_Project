from db.run_sql import run_sql

from controllers.manufacture_controller import manufactures

from models.product import Product
from models.manufacture import Manufacture


def save(manufacture):
    sql = "INSERT INTO manufactures(name) VALUES (%s) RETURNING id"
    values = [manufacture.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacture.id = id
    return manufacture

def select_all():
    manufacture = []

    sql = "SELECT * FROM manufactures"
    results = run_sql(sql)

    for row in results:
        manufacture = Manufacture(row['name'], row['id'])
        manufactures.append(manufacture)
    return manufactures

def select(id):
    manufacture = None
    sql = "SELECT * FROM manufactures WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacture = Manufacture(result['name'], result['id'])
    return manufacture


def products(manufacture):
    products = []

    sql = "SELECT products.* FROM products INNER JOIN products ON products.type_id = products.id WHERE manufacture_id = %s"
    values = [manufacture.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['name'], row['id'])
        products.append(product)    

def delete_all():
    sql = "DELETE FROM manufactures"
    run_sql(sql)