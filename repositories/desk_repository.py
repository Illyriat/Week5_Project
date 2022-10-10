from db.run_sql import run_sql

from models.desk import Desk
from models.manufacture import Manufacture

import repositories.manufacture_repository as manufacture_repository

def save(desk):
    sql = "INSERT INTO desks(model, description, stock_count, trade_price, sale_price, manufacture_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [desk.model, desk.description, desk.stock_count, desk.trade_price, desk.sale_price, desk.manufacture.id]
    results = run_sql(sql, values)
    desk.id = results[0]['id']
    return desk

def select_all():
    desks = []

    sql = "SELECT * FROM desks"
    results = run_sql(sql)

    for row in results:
        manufacture = manufacture_repository.select(row['manufacture_id'])
        desk = Desk(row['model'], row['descriptin'], row['stock_count'], row['trade_price'], row['sale_price'], row['id'], manufacture)
        desks.append(desk)
    return desks

def manufacture():
    sql = "SELECT * FROM manufactures WHERE id = %s"
    values = [desk.manufacture.id]
    results = run_sql(sql, values)[0]
    desk = Desk(results['model'], results['id'])
    return manufacture

def delete_all():
    sql = "DELETE FROM manufactures"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM desks WHERE id = %s"
    values = [id]
    run_sql(sql, values)
