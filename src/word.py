import requests
import json
import secrets

class Word:

    def __init__(self, word, definition, synonyms=[]):
        self.word = word
        self.definition = definition
        self._synonyms = synonyms



    @staticmethod
    def get_word_from_string(user_input):
        params = {
        "key": secrets.dictkey
         }

        response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{user_input}", params=params)
        word = json.loads(response.text)
      
        if word and isinstance(word[0], dict):
            word = Word(word[0]['meta']['stems'][0], word[0]['shortdef'][0])
            return word
        else:
            return None


    @property
    def synonyms(self):
        if self._synonyms:
            return self.synonyms
        else:
            # make API call
            # save response into self._synonyms
            # return self._synonyms
            pass
    

    def __str__(self):
        return f"{self.word}: {self.definition}"
    
    def __repr__(self):
        return f"{self.word}: {self.definition}"
    