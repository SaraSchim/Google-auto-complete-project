class AutoCompleteData:

    # type sub = 0, type change = 1, type add = 2, type remove = 3
    def __init__(self, sentence_index, index, type, len_of_input):
        self.__sentence_index = sentence_index
        self.__score = len_of_input*2
        if type != 0:
            if type == 3:
                type = 2
            if index > 4:
                self.__score -= type
            else:
                self.__score -= (5-index+1)*type

    def get_sentence(self):
        return self.__sentence_index

    def get_score(self):
        return self.__score

    def __gt__(self, other):
        return self.__score > other.__score
