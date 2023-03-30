import os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from callbacks import (
    start,
    like,
    dislike
)

TOKEN = os.environ.get('TOKEN')


def main():
    # updater
    updater = Updater(TOKEN)
    # dispatcher
    dispatcher = updater.dispatcher

    # handlers
    dispatcher.add_handler(handler=CommandHandler(command='start', callback=start))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('👍'), callback=like))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('👎'), callback=dislike))

    # satrt polling
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()