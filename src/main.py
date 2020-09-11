import display_utils
from word import Word

def word_lookup():
    user_input = input("Please enter your word >> ")
    word = Word.get_word_from_string(user_input)

    


options, items = display_utils.create_option_block()
items["Look up a word"] = word_lookup

display_utils.choice_loop(options)


