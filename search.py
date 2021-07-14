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
def change(sentence):
    for letter in sentence[::-1]:
        if current_node.get(letter) is None:
            if not change(sentence):
                return
        l
        current_node = current_node[letter]
    for i in range(len(current_node[" "])):
        print(i + 1, ".", lines[current_node[" "][i]])
def search(sentence):
    num_result_sentence=0
    current_node = data_base
    regex = re.compile('[^a-zA-Z\s]')
    sentence=regex.sub('', sen)
    sentence = sentence.lower()
    sentence ="".join(sentence.split(" "))

    for letter in sentence:
        if current_node.get(letter) is None:
            for i in current_node.keys():
                pass
            finish=0
            break
        current_node = current_node[letter]
    if finish:
        index_list=get_index_sentence(current_node[" "])
        if len(index_list)==5:
            parse_and_sort(index_list)
            return
        num_result_sentence=len(index_list)
    for i in range(len(sentence),0,-1):
        sentence=sentence[i]="*"
def get_index_sentence(aa):
    print("get_index_sentence",aa)
    return aa


def parse_and_sort(aa):
    print("parse_and_sort",aa)
def bb(current_node,list=[]):
    for i in current_node.keys():
        if current_node.get(" ") is None:
            bb(current_node[i],list)
        else:
            index_list = get_index_sentence(current_node[" "])
            list=set(list+index_list)
            list=[i for i in list]
            if len(list)>=5:
                parse_and_sort(list)
                return 

# lines=get_lines()
# data_base=get_data()
# sentence = input("please enter sentence:")
# search(sentence)
l={'t': {'h': {'i': {'s': {' ': [1, 2], 'i': {'s': {' ': [1, 2], 'c': {'a': {'t': {' ': [1]}}}, 'm': {'e': {'l': {'l': {'o': {'n': {' ': [2]}}}}}}}}}}}}, 'i': {'s': {' ': [1, 2], 'c': {'a': {'t': {' ': [1]}}}, 'm': {'e': {'l': {'l': {'o': {'n': {' ': [2]}}}}}}}}, 'c': {'a': {'t': {' ': [1]}}}, 'm': {'e': {'l': {'l': {'o': {'n': {' ': [2]}}}}}}}
bb(l)