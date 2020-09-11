from pathlib import Path
import json
from word import Word



class Data:

    data_location = Path.home().joinpath("DictionaryApp", "favourites.json")
    print(data_location)

    if data_location.is_file():
        with open(data_location, "") as data_file:
            favourites = json.load(data_file)
    else:
        favourites = []
    

    @classmethod
    def save_favourites(cls):
        with open(cls.data_location) as data_file:
            raw_data = json.dumps(cls.favourites)
            data_file.write(raw_data)
    
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
        else:
            print("Word is not in favourites.")

    

    



    




