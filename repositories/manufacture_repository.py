from db.run_sql import run_sql

from models.manufacture import Manufacture


def save(manufacture):
    sql = "INSERT INTO monufactures(name) VALUES (%) RETURNING id"
    values = [manufacture.name]
    results = run_sql(sql, values)
    manufacture.id = resul