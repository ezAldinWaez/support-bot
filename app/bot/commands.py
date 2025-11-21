from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import (
    BotCommand,
    BotCommandScopeChat,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllPrivateChats,
)

from app.bot.utils.texts import SUPPORTED_LANGUAGES
from app.config import Config


async def setup(bot: Bot, config: Config) -> None:
    """
    Set up bot commands for various scopes and languages.

    :param bot: The Bot object.
    :param config: The Config object.
    """
    # Define bot commands for different languages
    commands = {
        "en": [
            BotCommand(command="start", description="Restart bot"),
        ],
        "ar": [
            BotCommand(command="start", description="إعادة تشغيل البوت"),
        ]
    }

    if len(SUPPORTED_LANGUAGES) > 1:
        # If there are more than one supported language, add commands for changing the language
        commands["en"].append(
            BotCommand(command="language", description="Change language"),
        )
        commands["ar"].append(
            BotCommand(command="language", description="تغيير اللغة"),
        )

    group_commands = {
        "en": [
            BotCommand(command="ban", description="Block/Unblock a user"),
            BotCommand(command="silent", description="Activate/Deactivate silent Mode"),
            BotCommand(command="information", description="User information"),
        ],
        "ar": [
            BotCommand(command="ban", description="حظر/إلغاء حظر مستخدم"),
            BotCommand(command="silent", description="تفعيل/إلغاء الوضع الصامت"),
            BotCommand(command="information", description="معلومات المستخدم"),
        ]
    }

    admin_commands = {
        "en":
            commands["en"].copy() +
            [BotCommand(command="newsletter", description="Newsletter menu")],
        "ar":
            commands["ar"].copy() +
            [BotCommand(command="newsletter", description="قائمة النشرة")],
    }

    try:
        # Set commands for dev or admin in English language
        await bot.set_my_commands(
            commands=admin_commands["en"],
            scope=BotCommandScopeChat(chat_id=config.bot.DEV_ID),
        )
        # Set commands for dev or admin in Arabic language
        await bot.set_my_commands(
            commands=admin_commands["ar"],
            scope=BotCommandScopeChat(chat_id=config.bot.DEV_ID),
            language_code="ar",
        )
    except TelegramBadRequest:
        raise ValueError(f"Chat with DEV_ID {config.bot.DEV_ID} not found.")

    # Set commands for all private chats in English language
    await bot.set_my_commands(
        commands=commands["en"],
        scope=BotCommandScopeAllPrivateChats(),
    )
    # Set commands for all private chats in Arabic language
    await bot.set_my_commands(
        commands=commands["ar"],
        scope=BotCommandScopeAllPrivateChats(),
        language_code="ar",
    )
    # Set commands for all group chats in English language
    await bot.set_my_commands(
        commands=group_commands["en"],
        scope=BotCommandScopeAllGroupChats(),
    )
    # Set commands for all group chats in Arabic language
    await bot.set_my_commands(
        commands=group_commands["ar"],
        scope=BotCommandScopeAllGroupChats(),
        language_code="ar"
    )


async def delete(bot: Bot, config: Config) -> None:
    """
    Delete bot commands for various scopes and languages.

    :param config: The Config object.
    :param bot: The Bot object.
    """

    try:
        # Delete commands for dev or admin in any language
        await bot.delete_my_commands(
            scope=BotCommandScopeChat(chat_id=config.bot.DEV_ID),
        )
        # Delete commands for dev or admin in Arabic language
        await bot.delete_my_commands(
            scope=BotCommandScopeChat(chat_id=config.bot.DEV_ID),
            language_code="ar",
        )
    except TelegramBadRequest:
        raise ValueError(f"Chat with DEV_ID {config.bot.DEV_ID} not found.")

    # Delete commands for all private chats in any language
    await bot.delete_my_commands(
        scope=BotCommandScopeAllPrivateChats(),
    )
    # Delete commands for all private chats in Arabic language
    await bot.delete_my_commands(
        scope=BotCommandScopeAllPrivateChats(),
        language_code="ar",
    )
    # Delete commands for all group chats in any language
    await bot.delete_my_commands(
        scope=BotCommandScopeAllGroupChats(),
    )
    # Delete commands for all group chats in Arabic language
    await bot.delete_my_commands(
        scope=BotCommandScopeAllGroupChats(),
        language_code="ar",
    )