import telebot
from telebot import types
import os
import essentials
import config
#Create Bot.
bot = telebot.TeleBot(config.token)

def faqs_main(call):
     markup = types.InlineKeyboardMarkup()
     #next = types.InlineKeyboardButton('Next', callback_data='nexttrig')
     #back = types.InlineKeyboardButton('Back', switch_inline_query="backbsc")
     home = types.InlineKeyboardButton('Back to Main documentation', callback_data="home")
     #markup.row(next)
     markup.row(home)
     bot.edit_message_text(text = '''
*Frequently Asked Questions:*\n	      
    
*How can I use this bot?*

Well maybe you're too impatient to start with things. But the first line of the About text very well say that this is an inline bot. You can use this in any chat you want. Simply type the username of the bot and enter the *RIGHT* syntax to get the desired output.

*Will this allow me to skip school/college/institution/job ? *

Ah..there are certain things in life which are close to being referred to as "Impossible" :/ I'm sorry this bot cannot help you in skipping your real life activities.

 ''',parse_mode="Markdown",disable_web_page_preview="True", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)






