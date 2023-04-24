import sys
from AiW_Solver import AiWSolver

if __name__ == "__main__":
    if len(sys.argv) == 1:
        input_file = "input.txt"
        dictionary_file = "aliceInWonderlandDictionary.txt"
    elif len(sys.argv) == 2:
        input_file = sys.argv[1]
        dictionary_file = "aliceInWonderlandDictionary.txt"
    elif len(sys.argv) == 3:
        input_file = sys.argv[1]
        dictionary_file = sys.argv[2]
    else:
        sys.stderr.write("""Improper Usage Error: 'python3 main.py' or 'python3 main.py [input.txt]' 'python3 main.py [input.txt] [dictionary.txt]""")
        exit(1)

    word_solver = AiWSolver()
    word_solver.load_input_strings(input_file)
    word_solver.load_dictionary_words(dictionary_file)
    print(word_solver)

