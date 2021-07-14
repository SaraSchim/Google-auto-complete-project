import json
import re

def get_data():
    with open('database.json', "r") as DB_file:
        data_base=json.load(DB_file)
    return data_base

def get_lines():
    with open('database_lines.json', "r") as DB_file:
        lines = json.load(DB_file)
    return lines

def search():
    current_node = data_base
    sen=input("please enter sentence:")
    regex = re.compile('[^a-zA-Z]' + '\s')
    regex.sub('', sen)
    sen = sen.lower()
    sen ="".join(sen.split(" "))
    for letter in sen:
        if current_node.get(letter) is None:
            print("nothing")
            print(letter)
            return
        current_node = current_node[letter]
    print(current_node[" "])
    for i in range(len(current_node[" "])):
        print(i+1,". ",lines[current_node[" "][i]])

lines=get_lines()
data_base=get_data()
search()