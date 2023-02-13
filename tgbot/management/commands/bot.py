from django.core.management.base import BaseCommand

from tgbot import handlers
from tgbot.services.application import get_telegram_application, add_command_handlers

COMMAND_HANDLERS = {
    'start': handlers.start,
    'help': handlers.help_,
}


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        print('AstroBot running')

        application = get_telegram_application()
        add_command_handlers(application, COMMAND_HANDLERS)
        application.run_polling()
