from search import print_result, machine_search


def main():
    sentence = input("Enter your text:")
    while sentence != "#":
        print_result(machine_search(sentence))
        sentence = input(sentence)
    return


if __name__ == '__main__':
    main()


