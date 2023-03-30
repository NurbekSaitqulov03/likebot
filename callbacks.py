from telegram.ext import CallbackContext
from telegram import Update
from db import DB

db = DB()

def start(update: Update, context: CallbackContext):
    # add user into database
    chat_id = update.message.chat.id
    db.add(chat_id)
    # send welcome message
    fullname = update.message.from_user.full_name
    update.message.reply_html(text=f'hello, <b>{fullname}</b>\n<i>Welcome to our bot!</i>')


def like(update: Update, context: CallbackContext):
    # increase like
    chat_id = update.message.chat.id
    data = db.increase_like(chat_id)
    # send number of your like and dislike
    update.message.reply_html(text=f'like: {data.get("like")}\ndislike: {data.get("dislike")}')

def dislike(update: Update, context: CallbackContext):
    # increase dislike
    chat_id = update.message.chat.id
    data = db.increase_dislike(chat_id)
    # send number of your like and dislike
    update.message.reply_html(text=f'like: {data.get("like")}\ndislike: {data.get("dislike")}')