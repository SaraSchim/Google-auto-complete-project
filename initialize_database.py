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


