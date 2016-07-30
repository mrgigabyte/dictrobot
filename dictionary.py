from telebot import types
import telebot
import io
import os
import essentials
from dictionaries import *
import help
import docs
import faqs 
import home
import config


bot = telebot.TeleBot(config.token)

if os.stat('privatelist').st_size == 0:
   privatelist = dict()
else:
   privatelist = essentials.load_dict('privatelist')

error = "sorry we're unable to find the required information:( \n"
def inline_error(msg):
    return types.InlineQueryResultArticle(str(1), 
        msg, message_text=error, description=error)
        
@bot.message_handler(func=lambda m: m.text=='/start')
def command_help(message):
    if message.chat.id not in privatelist.values():
      name = message.chat.first_name
      chat_id = message.chat.id
      essentials.add_key_dict('privatelist', privatelist, name, chat_id)     
    bot.send_message(message.chat.id, "*Hey there!* I'm a dictionary bot!\nWrite @dictrobot `<word>` to get the answer",parse_mode="Markdown")

#DOCS
@bot.message_handler(func=lambda message: message.text=='/docs' or message.text == '/start docs')
def command_help(message):
    docs.command_docs(message)

@bot.callback_query_handler(lambda q: q.data == 'faqs')
def handle_a_buton(call):
    faqs.faqs_main(call)

@bot.callback_query_handler(lambda q: q.data == 'home')
def handle_a_button(call):
     home.homebut(call)

#Inline Urban Dictionary
@bot.inline_handler(lambda q: q.query.split(' ')[0].lower() in ['.ud'] and len(q.query.split()) > 1)
def ud_query(q):
    try:
       results = ud.urbandictionary(q.query.split(' ', 1)[1])
    except Exception as e:
       print(e)
       results = [inline_error('Definition Not Found ._.')]
    bot.answer_inline_query(q.id, results, cache_time=1)

#Help
@bot.inline_handler(lambda q: q.query=="")
def query(q):    
    bot.answer_inline_query(q.id, help.help_result(), cache_time='1',switch_pm_text="How to use me ?",switch_pm_parameter="docs")

#English Dictionary
@bot.inline_handler(lambda q: True)
def d_query(q):
    try:
       results = eng.define_term(q.query)
    except Exception as e:
       print(e)
       results = [inline_error('Definition Not Found ._.')]
    bot.answer_inline_query(q.id, results, cache_time=1, switch_pm_text="How to use me?",switch_pm_parameter="docs")

@bot.message_handler(func=lambda message: True)
def command_help(message):
   if message.text == '/members':
    if message.chat.id == config.owner:
      bot.send_message(message.chat.id, len(privatelist))

print('[Bot started]')
bot.send_message(config.owner,'Bot Started')
bot.polling(none_stop=True)

