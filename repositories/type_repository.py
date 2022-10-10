from db.run_sql import run_sql

from models.type import Type
from models.manufacture import Manufacture

from repositories.product_repository import product

def save(type):
    sql = "INSERT INTO types(type) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [type.type, type.type_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    type.id = id
    return type

def select_all():
    types = []

    sql = "SELECT * FROM types"
    results = run_sql(sql)

    for row in results:
        product = product.select(row['manufacture_id'])
        type = Type(row['model'], row['descriptin'], row['stock_count'], row['trade_price'], row['sale_price'], row['id'], manufacture)
        types.append(type)
    return types

def manufacture():
    sql = "SELECT * FROM manufactures WHERE id = %s"
    values = [type.manufacture.id]
    results = run_sql(sql, values)[0]
    type = Type(results['model'], results['id'])
    return manufacture

def delete_all():
    sql = "DELETE FROM manufactures"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM types WHERE id = %s"
    values = [id]
    run_sql(sql, values)