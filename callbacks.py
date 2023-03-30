from telegram.ext import CallbackContext
from telegram import Update


def start(update: Update, context: CallbackContext):
    fullname = update.message.from_user.full_name
    update.message.reply_html(text=f'hello, <b>{fullname}</b>\n<i>Welcome to our bot!</i>')


def like(update: Update, context: CallbackContext):
    pass


def dislike(update: Update, context: CallbackContext):
    pass