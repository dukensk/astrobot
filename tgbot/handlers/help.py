from django.conf import settings
from django.template.loader import render_to_string

from telegram import Update
from telegram.ext import ContextTypes

from tgbot.handlers.response import send_response
from tgbot.services.template import render_template


async def help_(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_response(update, context, response=render_template('placeholder.html', {'update': update, 'context': context}))
