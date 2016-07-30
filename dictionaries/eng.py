import json
import requests
import random
from urllib.request import *
import html.parser    
from telebot import types


def define_term(query):   
   print('[English dictionary]')
   res = []
   url = 'https://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase={}&pretty=true'.format(query)
   requestSearch = requests.get(url).text       
   json_result = json.loads(requestSearch)
   result_list = json_result
   all_meanings = json_result['tuc'][0]['meanings']
   i = 1
   for item in all_meanings:
    text = html.parser.HTMLParser().unescape(item['text'])
    res.append(types.InlineQueryResultArticle(str(i),title=query, message_text = "*"+query+": *"+text,parse_mode="Markdown", description = text))
    i +=1
   return res

