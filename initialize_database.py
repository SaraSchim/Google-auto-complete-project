import json
import os
import re

data_base = dict()
lines = []


def insert(line, line_index):
    line = line.lower()
    line = line.split()
    for idx_first_word in range(len(line)):
        current_node = data_base
        for word in line[idx_first_word:len(line)]:
            for latter in word:
                if current_node.get(latter) is None:
                    current_node[latter] = dict()
                current_node = current_node[latter]
            if current_node.get(" ") is None:
                current_node[" "] = []
            current_node[" "].append(line_index)


def find_all_lines(root_path):
    count = 0
    # r=root, d=directories, f = files
    for r, d, f in os.walk(root_path):
        for file in f:
            if '.txt' in file:
                print(count)
                print(os.path.join(r, file))
                count += 1
                with open(os.path.join(r, file), "r", encoding="cp437", errors='ignore') as txt_file:
                    for line in txt_file.read().splitlines():
                        regex = re.compile('[^a-zA-Z\s]')
                        line=regex.sub('', line)
                        if len(line) >= 2:
                            lines.append(line)
                            insert(line, len(lines)-1)


def write_DB_to_file():
    path = '1'
    find_all_lines(path)
    with open('database.json', "w") as DB_file:
         json.dump(data_base, DB_file)
    with open('database_lines.json', "w") as DB_file:
         json.dump(lines, DB_file)


# write_DB_to_file()
insert("this is cat",1)
insert("this is mellon",2)
print(data_base)