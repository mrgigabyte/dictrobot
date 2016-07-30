import os


def load_list(file):
    'Returns a loaded file as a list.'
    temp_list = list()
    try:
        with open(file, 'r', encoding='utf8') as f:
            temp_list = eval(f.read())
        return temp_list
    
    except FileNotFoundError:
        print("filenotfounderror")


def create_dict(file, dict_name=None):
    'Returns a new created file as dictionary.'
    if dict_name == None:
        dict_name = dict()
        
    with open(file, 'a') as f:
        f.write(str(dict_name))
    print(file, 'created!')
    
    return dict_name

def load_dict(file):
    'Returns a loaded file as a dictionary.'
    temp_dict = dict()
    try:
        with open(file, 'r', encoding='utf8') as f:
            temp_dict = eval(f.read())
        return temp_dict
    
    except FileNotFoundError:
        return create_dict(file)

def save_dict(file, dict_name):
    'Saves a dictionary into a file.'  
    try:
        with open(file, 'w', encoding='utf8') as f:
            f.write(str(dict_name))
            
    except FileNotFoundError:
        create_dict(file, dict_name)

def add_key_dict(file, dict_name, key, val):
    'Adds a key and a value to the memory and saves it into a file.'
    dict_name[key] = val
    save_dict(file, dict_name)


