from  wonderwords import RandomWord #https://pypi.org/project/wonderwords/

wordsRW = RandomWord()
class words:
    
    @staticmethod
    def noun():
        return wordsRW.word(include_parts_of_speech=[words.KEY_NOUN])
    
    @staticmethod
    def adjective():
        return wordsRW.word(include_parts_of_speech=[words.KEY_ADJECTIVE])
    
    @staticmethod
    def verb():
        return wordsRW.word(include_parts_of_speech=[words.KEY_VERB])
    
    KEY_NOUN = "nouns"
    KEY_ADJECTIVE = "adjectives"
    KEY_VERB = "verbs"