from typing import Callable

from django.conf import settings

from telegram.ext import ApplicationBuilder, CommandHandler, Application


def get_telegram_application() -> Application:
    return ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()


def add_command_handlers(application: Application, command_handlers: dict[str, Callable]) -> None:
    for command_name, command_handler in command_handlers.items():
        application.add_handler(CommandHandler(command_name, command_handler))
