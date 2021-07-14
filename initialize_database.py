import os


def find_all_lines(root_path):
    lines = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(root_path):
        for file in f:
            if '.txt' in file:
                with open(os.path.join(r, file),"r", encoding="cp437", errors='ignore') as txt_file:
                    # print(txt_file.read().splitlines())
                    # print(txt_file.readlines())
                    for line in txt_file.read().splitlines():
                        if line != "":
                            lines.append(line)
    print(lines)


path = '2021-archive'
find_all_lines(path)

