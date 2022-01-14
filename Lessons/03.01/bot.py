import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

my_bot = telebot.TeleBot('5017490707:AAEKdLFu9IOHx-vIvUFqo_tVmGqLCLoiU9A')
print("my_bot is created")

@my_bot.message_handler(commands=['start','new'])
def start_message(message):
    print("start_message is working")
    my_bot.send_message(message.chat.id, 'hello!')

@my_bot.message_handler(commands=['curs'])
def curs_message(message):
    html = urlopen("https://kurs.onliner.by/")
    soup = BeautifulSoup(html)

    tags = soup.find_all('p', {'class':'value fall'})
    sell = tags[0].text
    buy = tags[1].text

    resp = f"банк покупает: {sell}; банк продаёт: {buy}"

    my_bot.send_message(message.chat.id, resp)


print("before polling")
my_bot.polling()
print("after polling")