from django.core.management.base import BaseCommand
from django.conf import settings

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


class Command(BaseCommand):
    # Used as command description usually
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        print('AstroBot running')

        async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            await update.message.reply_text(f'Hello {update.effective_user.first_name}')

        app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

        app.add_handler(CommandHandler("hello", hello))

        app.run_polling()
