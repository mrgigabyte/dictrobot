import io
import json
import urllib
from urllib.parse import *
from urllib.request import *
from telebot import types
md = ['`','*','_']

def ignore(text):
  if '*' in text:
    text = text.replace('*','\*')
  if '_' in text:
    text = text.replace('_','\_')
  if '`' in text:
    text = text.replace('`','\`')
  return text

def urbandictionary(text):
    searchQuery = text
    res = []
    #searchQuery = str(text[4:])
    if len(searchQuery):
        print('Urban Dictionary : ' + str(searchQuery))
        url = 'http://api.urbandictionary.com/v0/define?term=' + quote(searchQuery)
        req = Request(url, data=None)
        qResponse = urlopen(req)
        if qResponse.getcode() == 200:
            qJson = json.loads(qResponse.read().decode('utf-8'))
            if len(qJson['list']) <= 0:
                text1 = 'Sorry, I couldn\'t find anything on Urban Dictionary about the word '+text
                res.append(types.InlineQueryResultArticle(str(1),title="Not Found ._.", message_text = text1,parse_mode="Markdown", description = text1))
            else:
                #msg = 'Urban Dictionary on _' + searchQuery + '_\n\n*Definition*\n'
                msg = ""
                # Add definition of the word
                #print(qJson)
                i = 1
           
                for item in qJson['list']:
                 if qJson['list'].index(item)<8: 
                  msg = ""
                  title = item['word'] +' 👍 '+str(item['thumbs_up']) +'|👎'+str(item['thumbs_down'])
                  description = item['definition']
                  msg += '\n\n\n*Definition:* '+ignore(item['word'])+' \n' 
                  msg += ignore(item['definition'])
                  msg += '\n\n*Example*\n'
                  if len(item['example']):
                      msg += ignore(item['example'])
                  else:
                    msg += 'Not available'
                  #print(msg)
                  msg +='\n\n👍 '+str(item['thumbs_up']) +'|👎'+str(item['thumbs_down'])
                  res.append(types.InlineQueryResultArticle(str(i),title=title, message_text = msg,parse_mode="Markdown", description = description))
                  i +=1
                  
        else:
            print('Something went wrong! We got HTTP code: ' + str(qResponse.getcode()))
            
    else:
        text2 = 'Please enter a search query'
        res.append(types.InlineQueryResultArticle(str(1),title="Urban Dictionary", message_text = text2,parse_mode="Markdown", description = text2))
    return res   
        

