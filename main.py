# main.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from handlers.command_handlers import start, set_time, stats
from handlers.message_handlers import auto_delete_message
from config.config import BOT_TOKEN

def main():
    """Start the bot and add handlers."""
    updater = Updater(BOT_TOKEN, use_context=True)

    # Register handlers for commands
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("settime", set_time))
    updater.dispatcher.add_handler(CommandHandler("stats", stats))  # Add stats command

    # Register handler for all incoming text messages to auto-delete them
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_delete_message))

    # Start polling for updates
    updater.start_polling()

    # Run the bot until you stop it manually
    updater.idle()

if __name__ == "__main__":
    main()
