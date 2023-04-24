import sys
from Input_String import InputString
from Word import Word

class AiWSolver:
    def __init__(self):
        self.__input_strings = []
        self.__dictionary_words = []

    def get_input_strings(self):
        return self.__input_strings

    def get_dictionary_words(self):
        return self.__dictionary_words

    def set_input_strings(self, input_strings):
        self.__input_strings = input_strings

    def set_dictionary_words(self, dictionary_words):
        self.__dictionary_words = dictionary_words

    def add_input_string(self, string):
        self.get_input_strings().append(string)

    def add_dictionary_word(self, word):
        self.get_dictionary_words().append(word)

    def remove_input_string(self, string):
        self.get_input_strings().remove(string)

    def remove_dictionary_word(self, word):
        self.get_dictionary_words().remove(word)

    def load_input_strings(self, filename):
        try:
            with open(filename) as input_file:
                for line in input_file:
                    tmp_string = InputString(line.strip('\n'))
                    self.add_input_string(tmp_string)
        except FileNotFoundError:
            sys.stderr.write(
                '''Input file not found. Please verify the filename is correct and it is in the same directory as main.py''')
            exit(1)

    def load_dictionary_words(self, filename):
        try:
            with open(filename) as input_file:
                for line in input_file:
                    tmp_word = Word(line.strip('\n'))
                    self.add_dictionary_word(tmp_word)
        except FileNotFoundError:
            sys.stderr.write(
                '''Dictionary file not found. Please verify the filename is correct and it is in the same directory as main.py''')
            exit(1)

    def __str__(self):
        ret = 'Input Strings: \n'
        for string in self.get_input_strings():
            ret += f'{string}'

        for word in self.get_dictionary_words():
            ret += f'{word}\n'

        return ret
