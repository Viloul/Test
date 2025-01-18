# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# #Пример данных
# posts = [
#     {"id": 1, "title": "Первый пост", "body": "Тело первого поста"}
# ]
#
# # 1. Обработка GET-запроса (получить все посты)
# @app.route('/', methods=['GET'])
# def get_posts():
#     return jsonify(posts)
# # 2. Обработка POST-запроса (создать новый пост)
# @app.route('/', methods=['POST'])
# def create_post():
#     new_post = request.get_json() # Получаем JSON из тела запроса
#     for i in posts:
#         if i["id"] == new_post.get('id'):
#             return jsonify({"error": "id существует"}), 400
#     posts.append(new_post) # Добавляем новый пост в список
#     return jsonify(new_post),201 # Возвращаем новый пост и статус 201 (создано)
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8083)

# import sqlite3
#
# def create_table():
#     connection = sqlite3.connect('baza.db')
#     cursor = connection.cursor()
#     cursor.execute('''
#     CREATE TABLE users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL,
#         password TEXT NOT NULL,
#         email TEXT NOT NULL)
#     ''')
#     connection.commit()
#     connection.close()
#     print('Таблица успешно создана!')
#
# def add_user(username, password, email):
#     connection = sqlite3.connect('baza.db')
#     cursor = connection.cursor()
#         cursor.execute('''
#         INSERT INTO users (username, password, email)
#         VALUES (?,?,?)
#         ''', (username, password, email))
#         connection.commit()
#         connection.close()
#         print('Пользователь добавлен успешно!')
#
# def get_users():
#     connection = sqlite3.connect('baza.db')
#     cursor = connection.cursor()
#     cursor.execute('''
#     SELECT username, email FROM users
#     ''')
#     users = cursor.fetchall()
#     connection.close()
#     print('Список пользователей:')
#     for user in users:
#         print(user)
#
# def update_user(username, email):
#     connection = sqlite3.connect('baza.db')
#     cursor = connection.cursor()
#     cursor.execute('''
#     UPDATE users
#     SET email = ?
#     WHERE username = ?
#     ''', (email, username))
#     connection.commit()
#     connection.close()
#     print('Данные обновлены успешно!')
#
# def delete_user(username):
#     connection = sqlite3.connect('baza.db')
#     cursor = connection.cursor()
#     cursor.execute('''
#     DELETE FROM users
#     WHERE username = ?
#     ''', (username, ))
#     connection.commit()
#     connection.close()
#     print('Пользователь удален успешно!')
#
# if __name__ == '__main__':
#     # create_table()
#     add_user('test', 'test', 'test@test.test')
#     # add_user('test2', 'test2', 'test2@test.test')
#     # add_user('test3', 'test3', 'test3@test.test')
#     # get_users()
#     # update_user('test', 't@t.t')
#     # get_users()
#     # delete_user('test')
#     # get_users()

import datetime
import time

import telebot

from func import add_user, create_table, log_message

bot = telebot.TeleBot('7831552004:AAGsC6W5jLpB_FxaljAb8E-HqiYVUeIgznk')

@bot.message_handler(commands=['start'])
def start_message(message):
    add_user(message.from_user.id, message.from_user.username)
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    log_message(message.from_user.id, message.text)
    bot.send_message(message.chat.id, "Ваше сообщение сохранено в базе данных.")

while True:
    try:
        create_table()
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)