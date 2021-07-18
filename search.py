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


def go_down_db(current_node, len_sentence):
    global list, end
    if end == 0:
        for i in current_node.keys():
            if current_node.get(" ") is None:
                go_down_db(current_node[i], len_sentence)
            else:
                list += get_index_sentence(current_node[" "])
                # for idx in index_list:
                #     # print(idx)
                #     obj = AutoCompleteData(idx, -1, 0, len_sentence)
                #     list.append(obj)
                if len(list) >= 5:
                    end = 1


#thisis
def find_node_by_sentence(node, sentence):
    # print(sentence)
    global list, end
    for i in range(len(sentence)):
        if sentence[i] == "*":
            for key in node.keys():
                if key != " ":
                    result = find_node_by_sentence(node[key], sentence[i + 1:])
                    if result:
                        return result
            return False
        else:
            if not node.get(sentence[i]):
                go_down_db(node, i - 1)
                if end == 1:
                    end = 0
                    returned_list = list[:]
                    list = []
                    return returned_list
                return False
            node = node.get(sentence[i])
    if not node.get(" "):
        go_down_db(node, len(sentence))
        if end == 1:
            end = 0
            returned_list = list[:]
            list = []
            return returned_list
        return False
    return node.get(" ")


# print(find_node_by_sentence(data_base, "sis"))



def machine_search(sentence):
    regex = re.compile('[^a-zA-Z\s]')
    sentence = regex.sub('', sentence)
    sentence = sentence.lower()
    sentence = "".join(sentence.split(" "))
    last_node = find_node_by_sentence(data_base, sentence)
    array = get_index_sentence(last_node)
    print(array)
    if array:
        len_array = len(array)
        array = [AutoCompleteData(i, 0, 0, len(lines[i])) for i in array]
    else:
        len_array = 0
    if array and len(array) == 5:
        array = [i.get_sentence() for i in array]
        return parse_and_sort(array)
    else:
        change_list = fix_char(sentence, 5 - len_array, 1)
        add_list = fix_char(sentence, 5 - len_array, 2)
        print(add_list)
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




def parse_and_sort(sentences_list):
    result_list = [lines[i] for i in sentences_list]
    result_list.sort()
    return result_list


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
                obj = AutoCompleteData(i, char, type, len(sentence))
                result.append(obj)
                if len(result) >= num:
                    return result[:num]
    if result:
        return result
    return []


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


# TODO:
'''
snetences that do not work well:
thiis is
have a
problems:
double lines returned
'''
