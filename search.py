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



end=0
def go_down_db(current_node,sentence):
    global list,end
    if end==0:
        for i in current_node.keys():
            if current_node.get(" ") is None:
                go_down_db(current_node[i],sentence)
            else:
                index_list = get_index_sentence(current_node[" "])
                for idx in index_list:
                    print(idx)
                    obj = AutoCompleteData(idx, -1, 0, len(sentence))
                    list.append(obj)
                if len(list) >= 5:
                    end=1



def find_node_by_sentence(node, sentence):
    for i in range(len(sentence)):
        if sentence[i] == "*":
            for key in node.keys():
                result = find_node_by_sentence(node[key], sentence[i + 1:])
                if result:
                    return result
            return False
        else:
            if not node.get(sentence[i]):
                go_down_db(node, i-1)
                if end == 1:
                    return list
                return False
            node = node.get(sentence[i])
    return node.get(" ")


def machine_search(sentence):
    regex = re.compile('[^a-zA-Z\s]')
    sentence = regex.sub('', sentence)
    sentence = sentence.lower()
    sentence = "".join(sentence.split(" "))
    last_node = find_node_by_sentence(data_base, sentence)
    array = get_index_sentence(last_node)
    if array:
        len_array = len(array)
    else:
        len_array = 0
    if array and len(array) == 5:
        return parse_and_sort(array)
    else:
        change_list = fix_char(sentence, 5 - len_array, 1)
        add_list = fix_char(sentence, 5 - len_array, 2)
        remove_list = fix_char(sentence, 5 - len_array, 3)
        all_fix_list = change_list + add_list + remove_list
        all_fix_list.sort(reverse=True)
        if array:
            array += all_fix_list[:len_array]
        else:
            array = all_fix_list[:len_array]
        array = [i.get_sentence() for i in array]
        array = parse_and_sort(array)
        return array


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


def parse_and_sort(sentences_list):
    result_list = [lines[i] for i in sentences_list]
    result_list.sort()
    return result_list


# type change = 1, type add = 2, type remove = 3
def fix_char(sentence, num, type):
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
    return []


a = fix_char("ths", 3, 1)
a.sort(reverse=True)
a = [i.get_sentence() for i in a]
a = parse_and_sort(a)
print(a)


def main():
    sentence = input("Enter your text:")
    while sentence != "#":
        print(machine_search(sentence))
        sentence = input(sentence)
    return


main()
