import requests
import json
import secrets
class Word:

    def read_and_convert_json(path):
        response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}key={dictkey}")

        word = json.loads(response.text)

        print(word)


    @staticmethod
    def get_word_from_string(user_input):
        word = Word()
        word.name = "Banana"
        word.definition = "A delicious fruit"

        return word

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
        return f"{self.name}: {self.definition}"
    
    def favourite(self):
        #