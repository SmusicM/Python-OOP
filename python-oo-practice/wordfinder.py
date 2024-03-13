"""Word Finder: finds random words from a dictionary."""
import unittest
import random
class WordFinder:
    """
    Returns random word
    >>> wf = WordFinder("words.txt")
    >>> word = wf.random()
    >>> word in wf.words
    True
    """
    def __init__(self,path_to_file):
        self.words=self.read_words(path_to_file)
    def read_words(self,path_to_file):
        with open(path_to_file,"r") as file:
            words = [line.strip() for line in file]
            return words
    def random(self):
        return random.choice(self.words)
        
class SpecialWordFinder(WordFinder):
    """
    >>> swf = SpecialWordFinder("words.txt")
    >>> specialword = swf.random()
    >>> specialword in swf.words
    True
    """
    def __init__(self, path_to_file):
        super().__init__(path_to_file)
        self.words = [word for word in self.words
         if not word.startswith("#") and word]
        #filters words that we want and not with #
        #return self.words



