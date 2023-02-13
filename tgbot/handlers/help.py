from django.conf import settings

from telegram import Update
from telegram.ext import ContextTypes


async def help_(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'YOU DIED')
