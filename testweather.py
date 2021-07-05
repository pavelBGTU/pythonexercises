from pyowm import OWM
from pyowm.utils import config
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('ff7666ec5ee38c6689257e55fe50ca78', config_dict)
mgr = owm.weather_manager()
import telebot
bot = telebot.TeleBot("1405402021:AAHN4z7z-ihGCqCh33ylXirglCiUzwo7Ne4", parse_mode=None)
@bot.message_handler(content_types=['text'])

def send_echo(message):
	try:
		observation = mgr.weather_at_place(message.text)
	except Exception:
		bot.send_message(message.chat.id, "это не город")
	else:
		w = observation.weather
		temp = w.temperature('celsius')["temp"]
		answer = "В городе " + message.text + " сейчас " + str(w.detailed_status) + "." + "\n"
		answer += "температура " + str(temp) + "\n\n"

		bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True)
