class Word:
    def __init__(self, word):
        self.__word = word

    def get_word(self):
        return self.__word

    def set_word(self, word):
        self.__word = word

    def __str__(self):
        return self.get_word()