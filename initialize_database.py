import os

data_base=dict()
def insert(line,line_index):
    line=line.lower()
    line=line.split()
    for idx_first_word in range(len(line)):
        current_node = data_base
        for word in line[idx_first_word:len(line)]:
            for latter in word:
                if current_node.get(latter)==None:
                    current_node[latter]=dict()
                current_node=current_node[latter]
            if current_node.get(" ")==None:
                current_node[" "]=[]
            current_node[" "].append(line_index)

def find_all_lines(root_path):
    lines = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(root_path):
        for file in f:
            if '.txt' in file:
                with open(os.path.join(r, file), "r") as txt_file:
                    for line in txt_file.read().splitlines():
                        lines.append(line)
                        insert(line, len(lines))
    print(lines)


path = '2021-archive'
find_all_lines(path)


