class AutoCompleteData:

    # type change = 1, type add\remove = 2
    def __init__(self, sentence_index, index, type, len_of_input):
        self.__sentence_index = sentence_index
        self.__score = len_of_input*2
        if index >= 4:
            self.__score -= type
        else:
            self.__score -= (5-index)*type


    def get_sentence(self):
        return self.__sentence_index

    def get_score(self):
        return self.__score

    # type change = 1, type add\remove = 2
    # def update_score(self, index, type):
    #     if index >= 4:
    #         self.__score -= type
    #     else:
    #         self.__score -= (5-index)*type


