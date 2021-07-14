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


#########################


def search(sentence):
    num_result_sentence = 0
    current_node = data_base
    regex = re.compile('[^a-zA-Z\s]')
    sentence = regex.sub('', sentence)
    sentence = sentence.lower()
    sentence = " ".join(sentence.split(" "))

    sen_list = go_down_db(current_node, sentence)
    # num_result_sentence = len(sen_list)
    print(sen_list)


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


def change(sentence):
    for letter in sentence[::-1]:
        if current_node.get(letter) is None:
            if not change(sentence):
                return

        current_node = current_node[letter]

    return current_node[" "]


def add_char(sentence):
    for char in range(len(sentence), 0, -1):
        fixed_sentence = sentence.remove(sentence[char])
        node = data_base[sentence[0]]
        for i in sentence:
            node = node[sentence[i]]


def remove_char(sentence):
    for char in range(len(sentence), 0, -1):
        fixed_sentence = sentence[char] = "*"
        search(fixed_sentence)


def parse_and_sort(sentences_list):
    result_list = [lines[i] for i in sentences_list]
    result_list.sort()
    return result_list


list = []


def go_down_db(current_node):
    global list
    for i in current_node.keys():
        if current_node.get(" ") is None:
            go_down_db(current_node[i])
            print(i)
        else:
            index_list = get_index_sentence(current_node[" "])
            list = set(list + index_list)
            list = [i for i in list]
            print(list)
            if len(list) >= 5:
                parse_and_sort(list)
                return

            # lines=get_lines()

def go_down(sentence):
    node = data_base.get(sentence[0])
    i=1
    while node.get(sentence[i]):
        node = node.get(sentence[i])
        i+=1
        if i == len(sentence):
            return node[" "]
    return None




sentence = input("please enter sentence:")
print(go_down(sentence))
# search(sentence)
