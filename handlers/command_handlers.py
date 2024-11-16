# handlers/command_handlers.py
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from config.config import DELETE_TIME

# Global variable for deleted messages count
deleted_messages_count = 0

def start(update: Update, context: CallbackContext):
    """Send a welcome message when the bot starts."""
    update.message.reply_text("Hello! I will delete all messages (user and bot) after a specified time. Use /settime <seconds> to set a custom delete time.")

def set_time(update: Update, context: CallbackContext):
    """Set the global delete time for all messages."""
    global DELETE_TIME
    try:
        # Get the time from the command arguments (e.g., /settime 15)
        time_in_seconds = int(context.args[0])
        DELETE_TIME = time_in_seconds
        update.message.reply_text(f"Global delete time set to {time_in_seconds} seconds.")
    except (IndexError, ValueError):
        update.message.reply_text("Please provide a valid time in seconds, e.g., /settime 10.")

def stats(update: Update, context: CallbackContext):
    """Display the current deleted messages count."""
    update.message.reply_text(f"The bot has deleted {deleted_messages_count} messages so far.")
