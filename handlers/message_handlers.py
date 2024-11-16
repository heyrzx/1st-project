# handlers/message_handlers.py
import time
import threading
from telegram import Update
from telegram.ext import MessageHandler, Filters, CallbackContext
from config.config import DELETE_TIME

# Global variable for deleted messages count
deleted_messages_count = 0

messages_to_delete = {}

def auto_delete_message(update: Update, context: CallbackContext):
    """Automatically delete messages after the specified time."""
    global deleted_messages_count
    message_id = update.message.message_id
    chat_id = update.message.chat_id
    
    # Store message id and its timestamp in messages_to_delete
    messages_to_delete[message_id] = time.time()
    
    # Start a thread to delete the message after the specified time
    threading.Thread(target=delete_message_after_time, args=(chat_id, message_id)).start()


def delete_message_after_time(chat_id: int, message_id: int):
    """Delete the message after the specified time."""
    global deleted_messages_count
    time.sleep(DELETE_TIME)
    
    # Check if the message id is still in the dictionary
    if message_id in messages_to_delete:
        try:
            context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            deleted_messages_count += 1
        except Exception as e:
            print(f"Error deleting message {message_id}: {e}")
        
        # Remove the message from the dictionary
        del messages_to_delete[message_id]
