from pathlib import Path
import json
from word import Word

class Data:

    folder_location = Path.home().joinpath("DictionaryApp")
    folder_location.mkdir(parents=True, exist_ok=True)
    data_location = folder_location.joinpath("favourites.json")

    if data_location.is_file():
        with open(data_location, "r") as data_file:
            favourites = json.load(data_file)
            favourites = [Word(word["word"], word["definition"], word["_synonyms"]) 
            for word in favourites]

    else:
        favourites = []
    
    @classmethod
    def save_favourites(cls):
        with open(cls.data_location, "w") as data_file:
            
            raw_data = [word.__dict__ for word in cls.favourites]
            raw_data = json.dumps(raw_data)
            data_file.write(raw_data)
            print("Word successfully saved.")
    
    @classmethod
    def add_favourite(cls, word):
        if isinstance(word, Word):

            cls.favourites.append(word)
            cls.save_favourites()
        else:
            raise ValueError("Non word object cannot exist in favourites")
    
    @classmethod
    def remove_favourite(cls, word):
        if word in cls.favourites:
            cls.favourites.remove(word)
            cls.save_favourites()
        else:
            print("Word is not in favourites.")





    




