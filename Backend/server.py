from os import access

from flask import Flask, jsonify

app = Flask(__name__)
from sql_connection import get_sql_connection
import product_dao

connection = get_sql_connection()

@app.route("/getProducts")
def hello():
    products = product_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000, debug=True)
