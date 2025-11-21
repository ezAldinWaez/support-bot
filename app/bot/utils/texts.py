from abc import abstractmethod, ABCMeta

from aiogram.utils.markdown import hbold

# Add other languages and their corresponding codes as needed.
# You can also keep only one language by removing the line with the unwanted language.
SUPPORTED_LANGUAGES = {
    "en": "🇬🇧 English",
    "ar": "🇸🇾 العربية",
}


class Text(metaclass=ABCMeta):
    """
    Abstract base class for handling text data in different languages.
    """

    def __init__(self, language_code: str) -> None:
        """
        Initializes the Text instance with the specified language code.

        :param language_code: The language code (e.g., "ru" or "en").
        """
        self.language_code = language_code if language_code in SUPPORTED_LANGUAGES.keys() else "en"

    @property
    @abstractmethod
    def data(self) -> dict:
        """
        Abstract property to be implemented by subclasses. Represents the language-specific text data.

        :return: Dictionary containing language-specific text data.
        """
        raise NotImplementedError

    def get(self, code: str) -> str:
        """
        Retrieves the text corresponding to the provided code in the current language.

        :param code: The code associated with the desired text.
        :return: The text in the current language.
        """
        return self.data[self.language_code][code]


class TextMessage(Text):
    """
    Subclass of Text for managing text messages in different languages.
    """

    @property
    def data(self) -> dict:
        """
        Provides language-specific text data for text messages.

        :return: Dictionary containing language-specific text data for text messages.
        """
        return {
            "en": {
                "select_language": f"👋 <b>Hello</b>, {hbold('{full_name}')}!\n\nSelect language:",
                "change_language": "<b>Select language:</b>",
                "main_menu": "<b>Write your question</b>, and we will answer you as soon as possible:",
                "message_sent": "<b>Message sent!</b> Expect a response.",
                "message_edited": (
                    "<b>The message was edited only in your chat.</b> "
                    "To send an edited message, send it as a new message."
                ),
                "user_started_bot": (
                    f"User {hbold('{name}')} started the bot!\n\n"
                    "List of available commands:\n\n"
                    "• /ban\n"
                    "Block/Unblock user"
                    "<blockquote>Block the user if you do not want to receive messages from him.</blockquote>\n\n"
                    "• /silent\n"
                    "Activate/Deactivate silent mode"
                    "<blockquote>When silent mode is enabled, messages are not sent to the user.</blockquote>\n\n"
                    "• /information\n"
                    "User information"
                    "<blockquote>Receive a message with basic information about the user.</blockquote>"
                ),
                "user_restarted_bot": f"User {hbold('{name}')} restarted the bot!",
                "user_stopped_bot": f"User {hbold('{name}')} stopped the bot!",
                "user_blocked": "<b>User blocked!</b> Messages from the user are not accepted.",
                "user_unblocked": "<b>User unblocked!</b> Messages from the user are being accepted again.",
                "blocked_by_user": "<b>Message not sent!</b> The bot has been blocked by the user.",
                "user_information": (
                    "<b>ID:</b>\n"
                    "- <code>{id}</code>\n"
                    "<b>Name:</b>\n"
                    "- {full_name}\n"
                    "<b>Status:</b>\n"
                    "- {state}\n"
                    "<b>Username:</b>\n"
                    "- {username}\n"
                    "<b>Blocked:</b>\n"
                    "- {is_banned}\n"
                    "<b>Registration date:</b>\n"
                    "- {created_at}"
                ),
                "message_not_sent": "<b>Message not sent!</b> An unexpected error occurred.",
                "message_sent_to_user": "<b>Message sent to user!</b>",
                "silent_mode_enabled": (
                    "<b>Silent mode activated!</b> Messages will not be delivered to the user."
                ),
                "silent_mode_disabled": (
                    "<b>Silent mode deactivated!</b> The user will receive all messages."
                ),
            },
            "ar": {
                "select_language": f"👋 <b>مرحباً</b>، {hbold('{full_name}')}!\n\nاختر اللغة:",
                "change_language": "<b>اختر اللغة:</b>",
                "main_menu": "<b>اكتب سؤالك</b>، وسنجيبك في أقرب وقت ممكن:",
                "message_sent": "<b>تم إرسال الرسالة!</b> انتظر الرد.",
                "message_edited": (
                    "<b>تم تعديل الرسالة في محادثتك فقط.</b> "
                    "لإرسال الرسالة المعدلة، أرسلها كرسالة جديدة."
                ),
                "user_started_bot": (
                    f"المستخدم {hbold('{name}')} بدأ البوت!\n\n"
                    "قائمة الأوامر المتاحة:\n\n"
                    "• /ban\n"
                    "حظر/إلغاء حظر المستخدم"
                    "<blockquote>احظر المستخدم إذا كنت لا تريد استقبال رسائل منه.</blockquote>\n\n"
                    "• /silent\n"
                    "تفعيل/إلغاء الوضع الصامت"
                    "<blockquote>عند تفعيل الوضع الصامت، لا يتم إرسال الرسائل للمستخدم.</blockquote>\n\n"
                    "• /information\n"
                    "معلومات المستخدم"
                    "<blockquote>استلم رسالة تحتوي على المعلومات الأساسية عن المستخدم.</blockquote>"
                ),
                "user_restarted_bot": f"المستخدم {hbold('{name}')} أعاد تشغيل البوت!",
                "user_stopped_bot": f"المستخدم {hbold('{name}')} أوقف البوت!",
                "user_blocked": "<b>تم حظر المستخدم!</b> لن يتم قبول الرسائل من هذا المستخدم.",
                "user_unblocked": "<b>تم إلغاء حظر المستخدم!</b> سيتم قبول الرسائل من هذا المستخدم مجدداً.",
                "blocked_by_user": "<b>لم يتم إرسال الرسالة!</b> تم حظر البوت من قبل المستخدم.",
                "user_information": (
                    "<b>المعرف:</b>\n"
                    "- <code>{id}</code>\n"
                    "<b>الاسم:</b>\n"
                    "- {full_name}\n"
                    "<b>الحالة:</b>\n"
                    "- {state}\n"
                    "<b>اسم المستخدم:</b>\n"
                    "- {username}\n"
                    "<b>محظور:</b>\n"
                    "- {is_banned}\n"
                    "<b>تاريخ التسجيل:</b>\n"
                    "- {created_at}"
                ),
                "message_not_sent": "<b>لم يتم إرسال الرسالة!</b> حدث خطأ غير متوقع.",
                "message_sent_to_user": "<b>تم إرسال الرسالة للمستخدم!</b>",
                "silent_mode_enabled": (
                    "<b>تم تفعيل الوضع الصامت!</b> لن يتم توصيل الرسائل للمستخدم."
                ),
                "silent_mode_disabled": (
                    "<b>تم إلغاء الوضع الصامت!</b> سيستلم المستخدم جميع الرسائل."
                ),
            },
        }
