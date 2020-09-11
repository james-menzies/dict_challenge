import display_utils
from word import Word
from persistence import Data

def word_lookup():
    user_input = input("Please enter your word >> ")
    word = Word.get_word_from_string(user_input)
    if word:
     
        options, items = display_utils.create_option_block()
        items["Add to favourites"] = lambda : Data.add_favourite(word)
        items["Go back"] = lambda: None

        prompt = f"{word}\n\n\n Please choose an option:\n"
        choice = display_utils.list_selection(options, prompt=prompt)
        choice()
    else:
        print("Word not found!")
    input("Press ENTER to continue >> ")

def view_favourites():
    if Data.favourites:
        for word in Data.favourites:
            print(word)
    else:
        print("You have no favourites yet. You should add some...")
    
    input("Press ENTER to go back.")
    

options, items = display_utils.create_option_block()
items["Look up a word"] = word_lookup
items["See your favourite words"] = view_favourites

display_utils.choice_loop(options)
