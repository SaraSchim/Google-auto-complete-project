import json
import os

data_base = dict()


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
    lines = []
    count = 0
    # r=root, d=directories, f = files
    for r, d, f in os.walk(root_path):
        for file in f:
            if '.txt' in file:
                print(count)
                print(os.path.join(r, file))
                count +=1
                with open(os.path.join(r, file), "r",  encoding="cp437", errors='ignore') as txt_file:
                    for line in txt_file.read().splitlines():
                        if len(line) < 2:
                            lines.append(line)
                            insert(line, len(lines))



def write_DB_to_file():
    path = '2021-archive'
    # path = 'aaa'
    find_all_lines(path)
    with open('database.json', "w") as DB_file:
        json.dump(data_base, DB_file)


write_DB_to_file()
