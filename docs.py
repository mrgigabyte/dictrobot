import telebot
from telebot import types
import os
import essentials
import config
#Create Bot.
bot = telebot.TeleBot(config.token)

def command_docs(message):
    markup = types.InlineKeyboardMarkup()
    faqs =  types.InlineKeyboardButton('FAQs',callback_data='faqs')
    markup.row(faqs)
    bot.send_message(message.chat.id, '''
*Documentation:*
I'm an Inline Bot. You can use me to find meaning of words.

*Apparently I support the following dictionaries :*
`1`-English Dictionary
`2`-Urban  Dictionary

*How to use English dictionary ?*

Simply type the username followed by the word you want to search.
`Example:` @dictrobot Premonition

*How to use Urban Dictionary ?*

Simply type the username followed by `.ud [space] <word>`
`Example:` @dictrobot .ud lad

My creator will be adding more dictionaries soon! 
Please feel free to suggest him at @nandan
''',parse_mode="Markdown",reply_markup=markup)
