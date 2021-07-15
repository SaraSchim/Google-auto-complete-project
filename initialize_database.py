import json
import os
import re

data_base = dict()
lines = []


# file_name = 1


def insert(line, line_index):
    file_name = 1
    line = line.lower()
    line = line.split()
    for idx_first_word in range(len(line)):
        current_node = data_base
        for word in line[idx_first_word:len(line)]:
            for letter in word:
                if current_node.get(letter) is None:
                    current_node[letter] = dict()
                current_node = current_node[letter]
            if current_node.get(" ") is None:
                current_node[" "] = []
            if len(current_node[" "]) < 10 and type(current_node[" "]) == type([]):
                current_node[" "].append(line_index)
            elif len(current_node[" "]) == 10 :
                with open("DB_files\{}.txt".format(file_name), "a") as sen_file:
                    for i in current_node[" "]:
                        sen_file.write("{}\n".format(i))
                current_node[" "] = "{}.txt".format(file_name)
                file_name += 1
            else:
                with open("DB_files\{}".format(current_node[" "]), "a") as sen_file:
                    sen_file.write("{}\n".format(line_index))


def find_all_lines(root_path):
    count = 0
    # r=root, d=directories, f = files
    for r, d, f in os.walk(root_path):
        for file in f:
            if '.txt' in file:
                print(count)
                # print(os.path.join(r, file))
                count += 1
                with open(os.path.join(r, file), "r", encoding="cp437", errors='ignore') as txt_file:
                    lines_list = txt_file.read().splitlines()
                    for i in range(len(lines_list)):
                        regex = re.compile('[^a-zA-Z\s]')
                        clear_line = regex.sub('', lines_list[i])
                        lines_list[i] += ' ({} {})'.format(file[:-4], i)
                        if len(lines_list[i]) >= 2:
                            lines.append(lines_list[i])
                            insert(clear_line, len(lines) - 1)


def write_DB_to_file():
    print("Loading the files and preparing the system...")
    path = '1'
    # path = '2021-archive\python-3.8.4-docs-text'
    find_all_lines(path)
    with open('database.json', "w") as DB_file:
        json.dump(data_base, DB_file)
    with open('database_lines.json', "w") as DB_file:
        json.dump(lines, DB_file)
    print("The system is ready.", end="")


write_DB_to_file()
# insert("this is cat",1)
# insert("this is mellon",2)
# insert("this is ",3)
# insert("this  mellon",4)
# insert("this ",5)
# insert("ahis ",7)
# insert("thisis mellon",6)

# print(data_base)
