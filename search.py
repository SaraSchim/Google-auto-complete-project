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



lines=get_lines()
data_base=get_data()
list = []

#########################


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



def machine_search(sentence):
    global list
    num_result_sentence=0
    current_node = data_base
    regex = re.compile('[^a-zA-Z\s]')
    sentence=regex.sub('', sentence)
    sentence = sentence.lower()
    sentence ="".join(sentence.split(" "))

    for letter in sentence:
        if current_node.get(letter) is None:
            for i in current_node.keys():
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


def parse_and_sort(aa):
    print("parse_and_sort",aa)

# def get_index_sentence(node):
#     if type(node) == list:
#         if len(node) >= 5:
#             result_list = node[:5]
#             return result_list
#         else:
#             return node
#     else:
#         with open(node, "r") as file:
#             result_list = file.readlines()
#             if len(result_list) >= 5:
#                 return result_list[:5]
#             else:
#                 return result_list

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


def add_char(sentence):
    for char in range(len(sentence), 0, -1):
        fixed_sentence = sentence.remove(char)
        search(fixed_sentence)

# lines=get_lines()
# data_base=get_data()
# sentence = input("please enter sentence:")
# search(sentence)

def main():
    sentence=input("Enter your text:")
    while sentence!="#":
        machine_search(sentence)
        sentence=input(sentence)
    return
main()