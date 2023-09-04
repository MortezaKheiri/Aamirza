from itertools import permutations
from hazm import Normalizer, word_tokenize
import pandas as pd

# first Download Moin_Key_Words.txt
address = "the downloaded txt file address on your system"

dictionary = pd.read_fwf(address)

def is_meaningful(word):
    # Implement a function to check if a word is meaningful in Persian
    if(list(dictionary['اب']).count(word) > 0):
        return True
    else :
        return False
    
def get_meaningful_permutations(input_string):
    normalizer = Normalizer()
    normalized_input = normalizer.normalize(input_string)
    words = word_tokenize(normalized_input)
    
    meaningful_permutations = set()
    for word in words:
        for length in range(1, len(word) + 1):
            for perm in permutations(word, length):
                perm_word = ''.join(perm)
                if is_meaningful(perm_word):
                    meaningful_permutations.add(perm_word)
    
    return meaningful_permutations

input_string = input("Letters = ")
wordLength = int(input("Length = "))

while wordLength > 0 :
    result = get_meaningful_permutations(input_string)

    for r in result :
        if(len(r) == wordLength):
            print(r)
    wordLength = int(input("Length = "))
