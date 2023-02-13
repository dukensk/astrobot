from django.conf import settings

from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'firstname: {update.effective_user.first_name} \n'
                                    f'username: {update.effective_user.name} \n'
                                    f'user id: {update.effective_user.id} \n'
                                    f'chat id: {update.effective_chat.id} \n'
                                    f'chat name: {update.effective_chat.first_name} \n'
                                    )
