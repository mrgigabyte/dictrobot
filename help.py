from telebot import types
import essentials
storage_help = "txtfiles/help"
help = essentials.load_dict(storage_help)
helpthumb = {
'English Dictionary':'http://i.imgur.com/IVozT2d.png',
'Urban Dictionary':'http://i.imgur.com/ZOpf4uG.png',
}
def help_result():
    print('[inline help]')
    res = []
    #print(res)
    #Result id.
    i = 1
    for x in help.keys():
        text = help[x]
        m = text
        if "`" in text:
          m = m.replace("`","")
        res.append(types.InlineQueryResultArticle(str(i), x, text,parse_mode="Markdown",description=m,thumb_url=helpthumb[x]))
        i += 1
    #print(query)
    return res
 
