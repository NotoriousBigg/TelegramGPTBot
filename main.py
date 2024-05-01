import telebot
import requests
from telebot import types
#Replace the bot token here with your actual Telegram Bot token Obtained from bot father..
bot = telebot.TeleBot("7143813665:AAFGZOig2DoM8sWAh4tQJwUfRKuN2VERqiY")
#Code for Sending start message
@bot.message_handler(commands=['start','help'])
def send_help_message(message):
    startmess = """
Hello there, 
I am Infinity AI.
A chat Gpt bot written in python created by @EscaliBud .
Just send any message and I will give you a response.
Type /help or /start to get this message.
    """
    keyboard = types.InlineKeyboardMarkup()
    helpbutt = types.InlineKeyboardButton("HELP", url="https://t.me/EscaliBud")
    channelbutt = types.InlineKeyboardButton("CHANNEL", url="https://t.me/+eVD8089l-U82Nzhk")
    keyboard.add(helpbutt, channelbutt)
    bot.send_message(message.chat.id, startmess, reply_markup=keyboard)

#Code for Answering to all messages
#It uses the Gemini API
def reply_gptmess(message):
    try:
      url = f"https://dev-the-dark-lord0.pantheonsite.io/wp-admin/js/Apis/Gemini.php?message={message.text}"
      response = requests.get(url)
      if response.status_code == 200:
        answer = response.text
        #bot.send_chat_action(message.chat.id,"typing")
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
      else:
            bot.send_message(message.chat.id, "A fatal error occured. Please contact admin.")
    except Exception as e:
        bot.send_message(message.chat.id, f"The following error occured \n\n {e} .\nForward It to admin")
bot.infinity_polling()
