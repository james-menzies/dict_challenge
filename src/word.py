import requests

class Word:

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