class Bot:
    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        print(message)

    def say_name(self):
        print(self.name)


class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        self.url = url
        self.chat_id = chat_id
        super().__init__(name)

    def send_message(self, message):
        print(f"{self.name} Bot says {message} to chat {self.chat_id} using {self.url}")

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id


bot = Bot("ChatGPT")
bot.say_name()
bot.send_message("I'm ChatGPT")

telegram_bot = TelegramBot("TG")
telegram_bot.say_name()

telegram_bot.send_message("Hello")
telegram_bot.set_chat_id(11)

telegram_bot.send_message("Hello, chat 11!")
telegram_bot.set_url("chat.com")

telegram_bot.send_message("Hello everyone!")
