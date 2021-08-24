import json
import re
from AutoCompleteData import AutoCompleteData


# read the data (trie) from the file
def get_data():
    with open('database.json', "r") as DB_file:
        data_base = json.load(DB_file)
    return data_base


# read the list of all lines from the file
def get_lines():
    with open('database_lines.json', "r") as DB_file:
        lines = json.load(DB_file)
    return lines


# global variables
lines = get_lines()
data_base = get_data()
list = []
end = 0


#########################


# given a node, returns the 5 first indexes (if they exist) of the lines that contains the string of that node as a
# substring
def get_index_sentence(node):
    if type(node) == type([]):
        if len(node) >= 5:
            result_list = node[:5]
            return result_list
        else:
            return node
    elif type(node) == str:
        with open("DB_files\{}".format(node), "r") as file:
            result_list = file.read().splitlines()
            result_list = [int(x) for x in result_list]
            if len(result_list) >= 5:
                return result_list[:5]
            else:
                return result_list
    else:
        return False


# when ending a sentence in a node that doesn't have a " " child - the function goes down the DB till it finds a
# list of 5 lines that contain the sentence as a prefix
# if found - updates the global variable "end" to be 1
def go_down_db(current_node):
    global list, end
    if end == 0:
        for i in current_node.keys():
            if current_node.get(" ") is None:
                go_down_db(current_node[i])
            else:
                list += get_index_sentence(current_node[" "])
                if len(list) >= 5:
                    end = 1


# given a starting node and a sentence - the func goes down the DB from the node according to the sentence's letters
# till the end of the sentence
# returns the node where stopped
def find_node_by_sentence(node, sentence):
    global end, list
    end = 0
    list = []
    for i in range(len(sentence)):
        if sentence[i] == "*":
            for key in node.keys():
                if key != ' ':
                    result_list = find_node_by_sentence(node[key], sentence[i + 1:])
                    if result_list:
                        return result_list
            return False
        else:
            if not node.get(sentence[i]):
                if i == len(sentence) - 1:
                    go_down_db(node)
                    if end == 1:
                        return list
                return False
            node = node.get(sentence[i])
    if not node.get(" "):
        go_down_db(node)
        if end == 1:
            return list
        return False
    result_list = []
    index_list = get_index_sentence(node.get(" "))
    if len(index_list) < 5:
        for i in node.keys():
            if i != " ":
                go_down_db(node[i])
                if end == 1:
                    return index_list + list
    return index_list


# given a sentence, searches for 5 lines that contain the sentence
# if not found (or found less than 5) - fixes the sentence in various ways and searches by the fixed sentence
# returns the 5 lines that have the highest score
def machine_search(sentence):
    regex = re.compile('[^a-zA-Z\s]')
    sentence = regex.sub('', sentence)
    sentence = sentence.lower()
    sentence = "".join(sentence.split(" "))
    last_node = find_node_by_sentence(data_base, sentence)
    array = get_index_sentence(last_node)
    if array:
        len_array = len(array)
        array = [AutoCompleteData(i, 0, 0, len(sentence)) for i in array]
    else:
        len_array = 0
    if array and len(array) >= 5:
        array = [i.get_sentence() for i in array]
        return parse_and_sort(array)
    else:
        change_list = fix_char(sentence, 5 - len_array, 1)
        add_list = fix_char(sentence, 5 - len_array, 2)
        remove_list = fix_char(sentence, 5 - len_array, 3)
        all_fix_list = change_list + add_list + remove_list
        all_fix_list.sort()
        if array:
            array += all_fix_list[:5 - len_array]
        else:
            array = all_fix_list[:5 - len_array]
        array = [i.get_sentence() for i in array]
        array = parse_and_sort(array)
        return array


# given a list of indexes - finds the lines in those indexes and sorts the list in alphabetic order
def parse_and_sort(sentences_list):
    result_list = [lines[i] for i in sentences_list]
    result_list.sort()
    return result_list


# given a sentence with 1 mistake, a number of lines that is needed and a type of mistake
# fixes the sentence according to the type of mistake and searches for lines that contain the fixed sentences
# type change = 1, type add = 2, type remove = 3
def fix_char(sentence, num, type):
    result = []
    temp = 0
    if type == 1 or type == 2:
        temp = 1
    if type == 2:
        c = ""
    else:
        c = "*"
    for j in range(len(sentence), 0, -1):
        fixed_sentence = sentence[:j - temp] + c + sentence[j:]
        res = find_node_by_sentence(data_base, fixed_sentence)
        if res:
            index_list = get_index_sentence(res)
            for i in index_list:
                obj = AutoCompleteData(i, j, type, len(sentence))
                result.append(obj)
                if len(result) >= num:
                    return result[:num]
    if result:
        return result
    return []


# given an array of the result lines - prints them nicely...
def print_result(array):
    for i in range(len(array)):
        print("{}. {}".format(i + 1, array[i]))
