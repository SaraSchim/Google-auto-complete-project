import json
import re


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

<<<<<<< HEAD
lines=get_lines()
data_base=get_data()
list = []
=======
>>>>>>> e794fdfae3434eb745a1e91204e03e275b1d22d8

#########################

def find_node_by_sentence(sentence):
    node = data_base
    for i in sentence:
        #TODO: case "*"
        node = node.get(i)
        if not node:
            return None
    return node.get(" ")

print(find_node_by_sentence("is"))


def go_down_db(current_node):
    global list
    for i in current_node.keys():
        if current_node.get(" ") is None:
            go_down_db(current_node[i])
        else:
            index_list = get_index_sentence(current_node[" "])
            list=set(list+index_list)
            list=[i for i in list]
            if len(list)>=5:
                print(list)
                parse_and_sort(list)
                exit()


<<<<<<< HEAD

def machine_search(sentence):
    global list
    num_result_sentence=0
=======
def search(sentence):
    num_result_sentence = 0
>>>>>>> e794fdfae3434eb745a1e91204e03e275b1d22d8
    current_node = data_base
    regex = re.compile('[^a-zA-Z\s]')
    sentence = regex.sub('', sentence)
    sentence = sentence.lower()
    sentence = "".join(sentence.split(" "))

    for letter in sentence:
        if current_node.get(letter) is None:
            for i in current_node.keys():
<<<<<<< HEAD
                go_down_db()
            break
        current_node = current_node[letter]
    if len(list)<5:
        index_list=get_index_sentence(current_node[" "])
        # if len(index_list)==5:
        #     parse_and_sort(index_list)
        #     return
        num_result_sentence=len(index_list)
    for i in range(len(sentence),0,-1):
        sentence=sentence[i]="*"


def get_index_sentence(aa):
    print("get_index_sentence",aa)
    return aa
=======
                pass
            finish = 0
            break
        current_node = current_node[letter]
    if finish:
        index_list = get_index_sentence(current_node[" "])
        if len(index_list) == 5:
            parse_and_sort(index_list)
            return
        num_result_sentence = len(index_list)
    for i in range(len(sentence), 0, -1):
        sentence = sentence[i] = "*"


# def get_index_sentence(aa):
#     print("get_index_sentence", aa)
#     return aa
>>>>>>> e794fdfae3434eb745a1e91204e03e275b1d22d8


def parse_and_sort(aa):
    print("parse_and_sort", aa)


def get_index_sentence(node):
    if type(node) == list:
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
        return None

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
# def parse_and_sort(sentences_list):
#     result_list = [lines[i] for i in sentences_list]
#     result_list.sort()
#     return result_list


def add_char(sentence, num):
    result = []
    for char in range(len(sentence), 0, -1):
        fixed_sentence = sentence[:char] + sentence[char+1:]
        res = find_node_by_sentence(fixed_sentence)
        if res:
            result += get_index_sentence(res)
            if len(result) >= num:
                return result[:num]
    return None

print(add_char("iss", 5))

<<<<<<< HEAD
=======
list = []
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


>>>>>>> e794fdfae3434eb745a1e91204e03e275b1d22d8
# lines=get_lines()
# data_base=get_data()
# sentence = input("please enter sentence:")
# search(sentence)

<<<<<<< HEAD
def main():
    sentence=input("Enter your text:")
    while sentence!="#":
        machine_search(sentence)
        sentence=input(sentence)
    return
main()
=======
z = {'t': {'h': {'i': {'s': {' ': [1, 2, 3, 4, 5], 'i': {
    's': {' ': [1, 2, 3, 6], 'c': {'a': {'t': {' ': [1]}}}, 'm': {'e': {'l': {'l': {'o': {'n': {' ': [2, 6]}}}}}}}},
                             'm': {'e': {'l': {'l': {'o': {'n': {' ': [4]}}}}}}}}}},
     'i': {'s': {' ': [1, 2, 3], 'c': {'a': {'t': {' ': [1]}}}, 'm': {'e': {'l': {'l': {'o': {'n': {' ': [2]}}}}}}}},
     'c': {'a': {'t': {' ': [1]}}}, 'm': {'e': {'l': {'l': {'o': {'n': {' ': [2, 4, 6]}}}}}},
     'a': {'h': {'i': {'s': {' ': [7]}}}}}
go_down_db(z)


>>>>>>> e794fdfae3434eb745a1e91204e03e275b1d22d8
