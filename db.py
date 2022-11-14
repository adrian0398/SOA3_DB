#db.py
# pylint: disable=trailing-whitespace, line-too-long, missing-module-docstring, invalid-name, consider-using-f-string, import-error 
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    """
    Method for connecting to database.

    :return: connection
    """ 
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_gastos(month,year):
    """
    Method for gething montly expenses .

    :param month: month to analyze
    :param year: year to analyze 
    :return: montly expenses
    """ 
    conn = open_connection()
    with conn.cursor() as cursor:
        command="SELECT departamento,descripcion,DATE_FORMAT(fecha,'%Y-%m-%d') as fecha,monto,nombre FROM gastos WHERE MONTH(fecha) = " + str(month) + ' AND YEAR(fecha) = ' + str(year) + ' ORDER by fecha;'
        result = cursor.execute(command)
        gastos = cursor.fetchall()
        if result > 0:
            got_gastos = jsonify(gastos)
        else:
            got_gastos = jsonify([])
    conn.close()
    return got_gastos



def get_gastos_tot(month,year):
    """
    Method for gething montly expenses total.

    :param month: month to analyze
    :param year: year to analyze 
    :return: montly expenses total
    """ 
    conn = open_connection()
    with conn.cursor() as cursor:
        command = 'SELECT SUM(monto) as total FROM gastos WHERE MONTH(fecha) = ' + str(month) + ' AND YEAR(fecha) = ' + str(year) + ' ;'
        result = cursor.execute(command)
        gastos = cursor.fetchall()
        if result > 0:
            got_gastos = jsonify(gastos[0])
            
        else:
            got_gastos = jsonify([])
            
    conn.close()
    return got_gastos

def get_top_departamentos_gastos(month,year):
    """
    Method for gething top 3 montly expenses by department.

    :param month: month to analyze
    :param year: year to analyze 
    :return: top 3 montly expenses by department
    """ 
    conn = open_connection()
    with conn.cursor() as cursor:
        command = 'SELECT departamento, SUM(monto) as total FROM gastos WHERE MONTH(fecha) = ' + str(month) + ' AND YEAR(fecha) = ' + str(year) + ' GROUP by departamento ORDER by SUM(monto) DESC LIMIT 3;'
        result = cursor.execute(command)
        gastos = cursor.fetchall()
        if result > 0:
            got_gastos = jsonify(gastos)
        else:
            got_gastos = jsonify([])
    conn.close()
    return got_gastos

def add_gastos(gastos):
    """
    Method for adding expenses.

    :param gastos: expenses
    """ 
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO gastos (departamento,descripcion,fecha,monto,nombre) VALUES(%s, %s, %s, %s, %s)', (gastos["departamento"], gastos["descripcion"], gastos["fecha"], gastos["monto"], gastos["nombre"]))
    conn.commit()
    conn.close()
