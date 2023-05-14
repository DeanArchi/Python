def init_for_bot(self, name):
    self.name = name


def send_message_bot(self, message):
    print(message)


def say_name_bot(self):
    print(self.name)


def init_telegram_bot(self, name, url=None, chat_id=None):
    self.url = url
    self.chat_id = chat_id
    super(telegram_bot, self).__init__(name)


def send_mes_tg(self, message):
    print(f"{self.name} Bot says {message} to chat {self.chat_id} using {self.url}")


def set_url_tg(self, url):
    self.url = url


def set_chat_id_tg(self, chat_id):
    self.chat_id = chat_id


bot = type(
    'Bot',
    (),
    {
        '__init__': init_for_bot,
        'send_message': send_message_bot,
        'say_name': say_name_bot
    }
)

telegram_bot = type(
    'TelegramBot',
    (bot, ),
    {
        '__init__': init_telegram_bot,
        'send_message': send_mes_tg,
        'set_url': set_url_tg,
        'set_chat_id': set_chat_id_tg
    }
)


my_bot = bot("Chat")
my_bot.say_name()
my_bot.send_message("Hello I'm Chat")

tg_bot = telegram_bot("TG")
tg_bot.say_name()

tg_bot.send_message("Hello")
tg_bot.set_chat_id(5)

tg_bot.send_message("Hello, chat 5!")
tg_bot.set_url("chatik.com")

tg_bot.send_message("Hey there!")
