import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = "7831552004:AAGsC6W5jLpB_FxaljAb8E-HqiYVUeIgznk"
bot = telebot.TeleBot(API_TOKEN)

admins_id = [5744864118, 5778219771]
user_ids = []

def is_admin(user_id):
    return user_id in admins_id

@bot.message_handler(commands=['start'])
def menu_command(message):
    if message.from_user.id not in user_ids:
        user_ids.append(message.from_user.id)
    if is_admin(message.from_user.id):
        markups = InlineKeyboardMarkup()
        markups.row(
            InlineKeyboardButton("photo", callback_data="photo"),
            InlineKeyboardButton("audio", callback_data="audio")
        )
        markups.row(
            InlineKeyboardButton("document", callback_data="document"),
            InlineKeyboardButton("video", callback_data="video")
        )
        bot.send_message(message.chat.id, "Choose a number:", reply_markup=markups)
    else:
        bot.send_message(message.chat.id, "You are not admin!")

@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    if is_admin(message.from_user.id):
            for user_id in user_ids:
                try:
                    bot.send_message(user_id, message.text[10:])
                except Exception as e:
                    print(f"Failed to send message to {user_id}: {e}")
    else:
        bot.send_message(message.chat.id, "You are not admin!")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "photo":
        send_photo(call.message)
    elif call.data == "audio":
        send_audio(call.message)
    elif call.data == "document":
        send_document(call.message)
    elif call.data == "video":
        send_video(call.message)

@bot.message_handler(commands=['photo'])
def send_photo(message):
    try:
        with open('File/1.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="Вот ваше изображение!")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Файл изображения не найден!")

@bot.message_handler(commands=['audio'])
def send_audio(message):
    try:
        with open('File/1.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio, caption="Вот ваше аудио!")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Файл аудио не найден!")

@bot.message_handler(commands=['document'])
def send_document(message):
    try:
        with open('File/1.txt', 'rb') as document:
            bot.send_document(message.chat.id, document, caption="Вот ваш документ!")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Файл документа не найден!")

@bot.message_handler(commands=['video'])
def send_video(message):
    try:
        with open('File/1.mp4', 'rb') as video:
            bot.send_video(message.chat.id, video, caption="Вот ваше видео!")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Файл видео не найден!")

@bot.message_handler(commands=['delete'])
def delete_message(message):
    if is_admin(message.from_user.id):
        if message.reply_to_message:
            bot.delete_message(message.chat.id, message.reply_to_message.message_id)
            bot.send_message(message.chat.id, "Message deleted!")
        else:
            bot.send_message(message.chat.id, "Reply to the message you want to delete!")
    else:
        bot.send_message(message.chat.id, "You are not admin!")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error: {e}")