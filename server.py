# from flask import Flask, request, jsonify
# import hashlib
#
# app = Flask(__name__)
#
# user_db = {}
#
# @app.route("/api/register", methods=["POST"])
# def register():
#     data = request.json
#     username = data.get("username")
#     password = data.get("password")
#     if not username or not password:
#         return {"error": "Missing username or password"}, 400
#     if username in user_db:
#         return {"error": "User already exists"}, 400
#     user_db[username] = hashlib.sha256(password.encode()).hexdigest()
#     return {"message": "User registered successfully"}
#
# @app.route("/api/login", methods=["POST"])
# def login():
#     data = request.json
#     username = data.get("username")
#     password = data.get("password")
#     if not username or not password:
#         return {"error": "Missing username or password"}, 400
#     if username not in user_db:
#         return {"error": "User not found"}, 404
#     if user_db[username] == hashlib.sha256(password.encode()).hexdigest():
#         return {"message": "Login successful"}
#     return {"error": "Invalid password"}, 401
#
# @app.route("/users", methods=["GET"])
# def dane():
#     return jsonify(user_db), 200
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)

import sqlite3

def create_table():
    connection = sqlite3.connect('baza.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE products (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price TEXT NOT NULL,
        stock TEXT NOT NULL)
    ''')
    cursor.execute('''
   CREATE TABLE purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
       product_id TEXT NOT NULL,
       quantity TEXT NOT NULL,
       total_price TEXT NOT NULL)
   ''')
    connection.commit()
    connection.close()
    print('Таблица успешно создана!')

def add_products(product_id, total_price, quantity):
    connection = sqlite3.connect('baza.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO users (product_id, total_price, quantity)
    VALUES (?,?,?)
    ''', (product_id, total_price, quantity))
    connection.commit()
    connection.close()
    print('Продукт добавлен успешно!')
