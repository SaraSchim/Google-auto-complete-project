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


end = 0

def go_down_db(current_node):
    global list, end
    if end == 0:
        for i in current_node.keys():
            if current_node.get(" ") is None:
                go_down_db(current_node[i])
            else:
                list += get_index_sentence(current_node[" "])
                # for idx in index_list:
                #     # print(idx)
                #     obj = AutoCompleteData(idx, -1, 0, len_sentence)
                #     list.append(obj)
                if len(list) >= 5:
                    end = 1


#thisis
# def find_node_by_sentence(node, sentence):
#     # print(sentence)
#     global list, end
#     for i in range(len(sentence)):
#         if sentence[i] == "*":
#             for key in node.keys():
#                 if key != " ":
#                     result = find_node_by_sentence(node[key], sentence[i + 1:])
#                     if result:
#                         return result
#             return False
#         else:
#             if not node.get(sentence[i]):
#                 go_down_db(node)
#                 if end == 1:
#                     end = 0
#                     returned_list = list[:]
#                     list = []
#                     return returned_list
#                 return False
#             node = node.get(sentence[i])
#     if not node.get(" "):
#         go_down_db(node)
#         if end == 1:
#             end = 0
#             returned_list = list[:]
#             list = []
#             return returned_list
#         return False
#     return node.get(" ")

#th*sis
def find_node_by_sentence(node, sentence):
    global end,list
    end=0
    list=[]
    for i in range(len(sentence)):
        if sentence[i] == "*":
            for key in node.keys():
                if key!=' ':
                    result_list = find_node_by_sentence(node[key], sentence[i + 1:])
                    if result_list:
                        return result_list
            return False
        else:
            if not node.get(sentence[i]):
                if i == len(sentence)-1:
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
    # for idx in index_list:
    #     obj = AutoCompleteData(idx, -1, 0, len(sentence))
    #     result_list.append(obj)
    if len(index_list) < 5:
        for i in node.keys():
            if i != " ":
                go_down_db(node[i])
                if end == 1:
                    return index_list + list
    return index_list

# print(find_node_by_sentence(data_base, "th*sis"))


def machine_search(sentence):
    regex = re.compile('[^a-zA-Z\s]')
    sentence = regex.sub('', sentence)
    sentence = sentence.lower()
    sentence = "".join(sentence.split(" "))
    last_node = find_node_by_sentence(data_base, sentence)
    array = get_index_sentence(last_node)
    # print(array)
    if array:
        len_array = len(array)
        array = [AutoCompleteData(i, 0, 0, len(sentence)) for i in array]
        print([i.get_score() for i in array])
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
        print([i.get_score() for i in array])
        array = [i.get_sentence() for i in array]
        array = parse_and_sort(array)
        return array




def parse_and_sort(sentences_list):
    result_list = [lines[i] for i in sentences_list]
    result_list.sort()
    return result_list

# print(parse_and_sort([360, 576, 810, 33, 33, 139, 517, 139, 517, 139, 517]))


# print(parse_and_sort([7, 15, 37, 52, 53]))

# print(lines)
# print((get_index_sentence(find_node_by_sentence(data_base, "this"))))


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
    for char in range(len(sentence), 0, -1):
        fixed_sentence = sentence[:char - temp] + c + sentence[char:]
        res = find_node_by_sentence(data_base, fixed_sentence)
        if res:
            index_list = get_index_sentence(res)
            for i in index_list:
                print(char)
                obj = AutoCompleteData(i, char, type, len(sentence))
                print(obj.get_score())
                result.append(obj)
                if len(result) >= num:
                    return result[:num]
    if result:
        return result
    return []

# a=(fix_char("thsis", 5, 3))
# a=[i.get_sentence() for i in a]
#
# print(parse_and_sort(a))

def print_result(array):
    for i in range(len(array)):
        print("{}. {}".format(i + 1, array[i]))


# print(fix_char("thiis", 2, 2))


def main():
    sentence = input("Enter your text:")
    while sentence != "#":
        print_result(machine_search(sentence))
        sentence = input(sentence)
    return


main()

