from db.run_sql import run_sql

from models.mic import Mic
from models.manufacture import Manufacture


import repositories.manufacture_repository as manufacture_repository

def save(mic):
    sql = "INSERT INTO mics(model, description, stock_count, trade_price, sale_price, manufacture_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [mic.model, mic.description, mic.stock_count, mic.trade_price, mic.sale_price, mic.manufacture.id]
    results = run_sql(sql, values)
    mic.id = results[0]['id']
    return mic

def select_all():
    mics = []

    sql = "SELECT * FROM mics"
    results = run_sql(sql)

    for row in results:
        manufacture = manufacture_repository.select(row['manufacture_id'])
        mic = Mic(row['model'], row['descriptin'], row['stock_count'], row['trade_price'], row['sale_price'], row['id'], manufacture)
        mics.append(mic)
    return mics

def manufacture():
    sql = "SELECT * FROM manufactures WHERE id = %s"
    values = [mic.manufacture.id]
    results = run_sql(sql, values)[0]
    mic = Mic(results['model'], results['id'])
    return manufacture

def delete_all():
    sql = "DELETE FROM manufactures"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM mics WHERE id = %s"
    values = [id]
    run_sql(sql, values)