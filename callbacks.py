from telegram.ext import CallbackContext
from telegram import (
    Update, 
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def start(update: Update, context: CallbackContext):    
    # keyboard
    btn1 = InlineKeyboardButton(text='👍', callback_data='like button')
    btn2 = InlineKeyboardButton(text='👎', callback_data='dislike button')
    inline_keyboard = [
        [btn1, btn2]
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

    # send welcome message
    fullname = update.message.from_user.full_name
    update.message.reply_html(text=f'hello, <b>{fullname}</b>\n<i>Welcome to our bot!</i>',)
    update.message.reply_html(
        text='press one of the buttons',
        reply_markup=reply_markup
        )


def like_or_dislike(update: Update, context: CallbackContext):
    # increase like
    data = update.callback_query.data
    print(data)