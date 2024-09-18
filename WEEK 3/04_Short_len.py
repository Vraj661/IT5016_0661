"""
Program which Shorter length of words
Author = Vraj Prajapati
"""

def function(word1,word2):
    len_1 = len(word1)
    len_2 = len(word2)
    shorter_length = min(len_1, len_2)
    return shorter_length

word1 = str(input("Enter word 1:-"))
word2 = str(input("Enter word 2:-"))
print(function(word1,word2))