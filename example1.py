import telebot
from datetime import time, date, datetime
bot = telebot.TeleBot("977866849:AAE4KLi1uwuTVrzrB23vMLuFcYzWlTyXKUs")
@bot.message_handler(commands = ['para'])
def send_echo(message):
	list =[["206 - МСС Л" , "26 - Комплексный анализ", "206 - Комп. стат."], ["304 - Комплан", "304 - Комплан", "502 - Комп. Стат. П"], ["202 - MCC Л", "27 - Комплексный анализ" , "208 - MCC С", "207 - Куценко П"], ["220 Java", "220 Java", "509 - Комп. Стат. П"], ["203 - Boris", "204 - KucenKo л", "205 Boris"]]
	now = datetime.now()
	if now.time() < time(9, 0) and now.time() > time(0, 0):
		i = 0
		k = 0
	elif now.time() >= time(9, 0) and now.time() < time(11, 40):
		i = 1
		k = 0
	elif now.time() >= time(11, 40) and now.time() < time(13, 30):
		i = 2
		k = 0
	elif now.time() > time(13, 40) and now.date().weekday() == 2 and now.time() < time(20, 0):
		i = 3
		k = 0
	elif now.date().weekday() == 5 or now.date().weekday() == 6:
		k = -now.date().weekday()
		i = 0
	else:
		i = 0
		k = 1
	if message.from_user.first_name == "Alisha":
		bot.send_message(message.chat.id, list[now.date().weekday() + k][i] + ", Повелитель")
	elif message.from_user.first_name == "Алексей":
		bot.send_message(message.chat.id, list[now.date().weekday() + k][i] + ", персик мой")
	else:
		bot.send_message(message.chat.id, list[now.date().weekday() + k][i])
bot.polling(none_stop = True)
