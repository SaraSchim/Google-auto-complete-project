import json
import re
from AutoCompleteData import AutoCompleteData


def get_data():
    with open('database.json', "r") as DB_file:
        data_base = json.load(DB_file)
    return data_base


def get_lines():
    with open('database_lines.json', "r") as DB_file:
        lines = json.load(DB_file)
    return lines


lines = get_lines()
data_base = get_data()
score = 0

list = []


#########################

def find_node_by_sentence(node, sentence):
    for i in range(len(sentence)):
        if sentence[i] == "*":
            for key in node.keys():
                result = find_node_by_sentence(node[key], sentence[i + 1:])
                if result:
                    return result
            return False
        else:
            node = node.get(sentence[i])
            if not node:
                return False
    return node.get(" ")

a = "thiis is ca"

def go_down_db(current_node):
    global list
    for i in current_node.keys():
        if current_node.get(" ") is None:
            go_down_db(current_node[i])
        else:
            index_list = get_index_sentence(current_node[" "])
            list = set(list + index_list)
            list = [i for i in list]
            if len(list) >= 5:
                print(list)
                parse_and_sort(list)
                exit()


def machine_search(sentence):
    global list
    len_sentence = len(sentence)
    current_node = data_base
    regex = re.compile('[^a-zA-Z\s]')
    sentence = regex.sub('', sentence)
    sentence = sentence.lower()
    sentence = "".join(sentence.split(" "))

    for letter in sentence:
        if current_node.get(letter) is None:
            for i in current_node.keys():
                go_down_db()
            break
        current_node = current_node[letter]
    if len(list) < 5:
        index_list = get_index_sentence(current_node[" "])
        # if len(index_list)==5:
        #     parse_and_sort(index_list)
        #     return
    for i in range(len(sentence) - 1, 0, -1):
        array = find_node_by_sentence(sentence[:i] + "*" + sentence[i + 1:])
        if array:
            pass




def get_index_sentence(node):
    if type(node) == type([]):
        if len(node) >= 5:
            result_list = node[:5]
            return result_list
        else:
            return node
    elif type(node) == str:
        with open(node, "r") as file:
            result_list = file.readlines()
            if len(result_list) >= 5:
                return result_list[:5]
            else:
                return result_list
    else:
        return False


#
# def change(sentence):
#     for letter in sentence[::-1]:
#         if current_node.get(letter) is None:
#             if not change(sentence):
#                 return
#
#         current_node = current_node[letter]
#
#     return current_node[" "]

#
def parse_and_sort(sentences_list):
    result_list = [lines[i] for i in sentences_list]
    result_list.sort()
    return result_list


# type change = 1, type add = 2, type remove = 3
def add_or_remove_char(sentence, num, type):
    result = []
    temp = 0
    if type == 1:
        temp = 1
    if type == 2:
        c = ""
    else:
        c = "*"
    for char in range(len(sentence), 0, -1):
        fixed_sentence = sentence[:char - temp] + c + sentence[char:]
        res = find_node_by_sentence(data_base, fixed_sentence)
        if res:
            index_list = get_index_sentence(res)
            for i in index_list:
                obj = AutoCompleteData(i, char, type, len(sentence))
                result.append(obj)
                if len(result) >= num:
                    return result[:num]
    if result:
        return result
    return None, 0


print(add_or_remove_char("ths", 3, 3))


# lines=get_lines()
# data_base=get_data()
# sentence = input("please enter sentence:")
# search(sentence)

def main():
    sentence = input("Enter your text:")
    while sentence != "#":
        machine_search(sentence)
        sentence = input(sentence)
    return
