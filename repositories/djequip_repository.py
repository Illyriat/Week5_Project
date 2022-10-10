from db.run_sql import run_sql

from models.djequip import Djequip
from models.manufacture import Manufacture

import repositories.manufacture_repository as manufacture_repository

def save(djeuip):
    sql = "INSERT INTO djequips(model, description, stock_count, trade_price, sale_price, manufacture_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [djeuip.model, djeuip.description, djeuip.stock_count, djeuip.trade_price, djeuip.sale_price, djeuip.manufacture.id]
    results = run_sql(sql, values)
    djeuip.id = results[0]['id']
    return djeuip

def select_all():
    djequips = []

    sql = "SELECT * FROM djequips"
    results = run_sql(sql)

    for row in results:
        manufacture = manufacture_repository.select(row['manufacture_id'])
        djequip = Djequip(row['model'], row['descriptin'], row['stock_count'], row['trade_price'], row['sale_price'], row['id'], manufacture)
        djequips.append(djequip)
    return djequips

def manufacture():
    sql = "SELECT * FROM manufactures WHERE id = %s"
    values = [djequip.manufacture.id]
    results = run_sql(sql, values)[0]
    djequip = Djequip(results['model'], results['id'])
    return manufacture

def delete_all():
    sql = "DELETE FROM manufactures"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM djequips WHERE id = %s"
    values = [id]
    run_sql(sql, values)