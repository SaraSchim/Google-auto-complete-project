
data_base=dict()
def sereach():
    current_node = data_base
    sen=input("please enter senteance:")
    sen = sen.lower()
    sen = sen.split()
    for letter in sen:
        if current_node.get(letter) is None:
            print("nothing")
        current_node = current_node[letter]
    return current_node[" "]