from db.run_sql import run_sql

from controllers.manufacture_controller import manufactures
from models.djequip import Djequip
from models.mic import Mic
from models.desk import Desk
from models.manufacture import Manufacture


def save(manufacture):
    sql = "INSERT INTO manufactures(name) VALUES (%) RETURNING id"
    values = [manufacture.name]
    results = run_sql(sql, values)
    manufacture.id = results[0]['id']
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


def desks(manufacture):
    desks = []

    sql = "SELECT desks.* FROM desks INNER JOIN desks ON desks.desk_id = desks.id WHERE manufacture_id = %s"
    values = [manufacture.id]
    results = run_sql(sql, values)

    for row in results:
        desk = Desk(row['name'], row['id'])
        desks.append(desk)

def mics(manufacture):
    mics = []

    sql = "SELECT mics.* FROM mics INNER JOIN mics ON mics.mic_id = mics.id WHERE manufacture_id = %s"
    values = [manufacture.id]
    results = run_sql(sql, values)

    for row in results:
        mic = Mic(row['name'], row['id'])
        mics.append(mic)   

def djequip(manufacture):
    djequips = []

    sql = "SELECT djequips.* FROM djequips INNER JOIN djequips ON djequips.djequip_id = djequips.id WHERE manufacture_id = %s"
    values = [manufacture.id]
    results = run_sql(sql, values)

    for row in results:
        djequip = Djequip(row['name'], row['id'])
        djequips.append(djequip)     

def delete_all():
    sql = "DELETE FROM manufactures"
    run_sql(sql)