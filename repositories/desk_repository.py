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