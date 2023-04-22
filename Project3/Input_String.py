class InputString:
    def __init__(self, input_text):
        self.__input_text = input_text
        self.__word_count = 0
        self.__aiW_Words = []

    def get_input_text(self):
        return self.__input_text

    def get_word_count(self):
        return self.__word_count

    def get_AiW_Words(self):
        return self.__aiW_Words

    def set_input_text(self, input_text):
        self.__input_text = input_text

    def set_word_count(self, word_count):
        self.__word_count = word_count

    def set_aiW_Words(self, words):
        self.__aiW_Words = words

    def add_aiW_Word(self, word):
        self.get_AiW_Words().append(word)

    def remove_aiW_Word(self, word):
        self.get_AiW_Words().remove(word)

    def __str__(self):
        ret = f'{self.get_input_text()} '

        if self.get_word_count() <= 0:
            ret += 'cannot be split into AiW words.'
            return ret
        else:
            ret += f'can be split into {self.get_word_count()}: '
            for word in self.get_aIW_Words():
                ret += f'{word} \n'

            return ret
