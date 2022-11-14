# pylint: disable= trailing-whitespace, line-too-long, missing-module-docstring, invalid-name, consider-using-f-string, unused-import, import-error, wrong-import-order 

from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask_cors import CORS, cross_origin

from db import get_gastos, get_top_departamentos_gastos, get_gastos_tot, add_gastos

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/gastos_mensuales", methods = ['GET'])
def get_gastos_mes():
    """
    Get montly expenses .

    :return: response
    """ 
    month = request.args.get("month")
    year = request.args.get("year")
    response=get_gastos(month,year)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/mayores_gastos_deps", methods = ['GET'])
def get_departamento_gastos_mayores():
    """
    Get Top 3 Expenses by Department .

    :return: response
    """ 
    month = request.args.get("month")
    year = request.args.get("year")
    response=get_top_departamentos_gastos(month,year)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/gastos_totales", methods = ['GET'])
def get_gastos_totales():
    """
    Get montly expenses total.
 
    :return: response
    """ 
    month = request.args.get("month")
    year = request.args.get("year")
    response=get_gastos_tot(month,year)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/gastos", methods = ['POST'])
def modify_gastos():
    """
    Post gastos.

    :return: {ok='true'} or error
    """ 
    print(request.get_json())
    add_gastos(request.get_json())
    response=jsonify(ok='true')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()
