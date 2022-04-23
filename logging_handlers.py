import logging
import telegram


class TelegramLogsHandler(logging.Handler):

    def __init__(self, tg_bot_token, admin_chat_id) -> None:
        super().__init__()
        self.tg_bot = telegram.Bot(token=tg_bot_token)
        self.chat_id = admin_chat_id
    
    def emit(self, record) -> None:
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)
