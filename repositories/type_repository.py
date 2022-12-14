from db.run_sql import run_sql

from models.type import Type
from models.manufacture import Manufacture

from repositories.product_repository import product

def save(type):
    sql = "INSERT INTO types(name) VALUES (%s) RETURNING *"
    values = [type.type]
    results = run_sql(sql, values)
    type.id = results[0]['id']
    return type

def select_all():
    types = []

    sql = "SELECT * FROM types"
    results = run_sql(sql)

    for row in results:
        type = Type(row['name'], row['id'])
        types.append(type)
    return types

def select(id):
    type = None
    sql = "SELECT * FROM types WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        type = Type(result['name'], result['id'])
    return type

def delete_all():
    sql = "DELETE FROM types"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM types WHERE id = %s"
    values = [id]
    run_sql(sql, values)