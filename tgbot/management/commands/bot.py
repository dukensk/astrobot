from django.core.management.base import BaseCommand
from django.conf import settings

from telegram.ext import ApplicationBuilder, CommandHandler

from tgbot.handlers.commands import start, help


class Command(BaseCommand):
    # Used as command description usually
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        print('AstroBot running')

        app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

        app.add_handler(CommandHandler('start', start))
        app.add_handler(CommandHandler('help', help))

        app.run_polling()
