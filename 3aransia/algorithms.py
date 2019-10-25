import pandas as pd
import nltk

from constants import *

# Translate Moroccan to Arabic
def moroccan_to_arabic(_str):
    alphabet = pd.read_csv('data/' + MOROCCAN_ALPHABET, usecols=['MoroccanAlphabet','ArabianAlphabet'])
    arabian_translation = []
    for word in _str.split():
        arabian_word = []
        word_iterator = iter(range(len(word)))
        for i in word_iterator:
            for (m, a) in zip(alphabet['MoroccanAlphabet'], alphabet['ArabianAlphabet']):
                if word[i] == 'c':
                    if i != len(word) and word[i+1] == 'h':
                        arabian_word.append('ش')
                        next(word_iterator)
                        break
                if word[i] == m:
                    arabian_word.append(a)
                    break
        arabian_translation.append((word, (''.join(arabian_word[::-1]).replace(u'\u200e', ''))))
    
    # return ' '.join(arabian_translation[::-1])
    return arabian_translation

# Translate Arabic to Moroccan


# Function to compute the distance between two words
def word_distance(word_1, word_2):
    return nltk.edit_distance(word_1, word_2)
    
# Converte a letter to its substitute
def letter_to_substitute(l):
    if l == '7': 
        return 'h'
    elif l == '9': 
        return 'q'
    else : 
        return l

# Word counter
def word_count(_str):
    counts = dict()
    words = _str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# Get duplicated
def generate_duplicates(_str):
    return dict(filter(lambda x:x[1] > 1, word_count(_str).items()))

# Generate lexically close words
def generate_close_words(threshold, _str):
    words = set()
    for w in _str.split():
        for y in _str.split():
            if w != y and word_distance(w,y) < threshold: 
                words.add((w,y, word_distance(w,y)))
    return sorted(words, key=lambda x:len(x[0]))

# Converte a word to its substitute
def word_to_substitute(word):
    return ''.join(list(map(lambda x:letter_to_substitute(x), word)))

# Validate Latin/Digit Moroccan to Arabic dictionary
def validate_dictionary(dictionary):
    data = pd.read_csv(dictionary)
    return data
    #TODO

# Temporary function to test
def run_tests():
    print(word_to_substitute('7alwa'))
    print(word_to_substitute('9o9o'))
    print(validate_dictionary('data/' + OPEN_DICTIONARY))
    print(word_distance("7alwa", "halwa"))
    print(word_distance("Halwa", "halwa"))
    print(generate_close_words(2, ''' 3aransia 3ebass 3la 3lache 3lak 3jbek ach achno 
ahlen alkhir allah amine amine ana ana ans atkounou awedi aychre7 b9aw ba bikher 
casa chadha couiya course da7k daba dakchi de7k dial dwa et ewa fen fin fin 
ghi had hada hadi hamdolillah hmd hmed hna ilyass incha inshaallah inshaallah iyeh 
jme3te kanmote khbar kidayer l3dou la3be lek lhal li lmoute lwer9a ma3autechlik 
makaynch man mazal men mezian n3ass nass nour nta ounta parcours pieds plus rah 
rak rani sa3a sa7bi sa7eb sahlen sbah sidi tan3ess tou7achnak twelef wata yhfde yhfdek zine'''))
    print(moroccan_to_arabic(''' 3aransia 3ebass 3la 3lache 3lak 3jbek ach achno 
ahlen alkhir allah amine amine ana ana ans atkounou awedi aychre7 b9aw ba bikher 
casa chadha couiya course da7k daba dakchi de7k dial dwa et ewa fen fin fin 
ghi had hada hadi hamdolillah hmd hmed hna ilyass incha inshaallah inshaallah iyeh 
jme3te kanmote khbar kidayer l3dou la3be lek lhal li lmoute lwer9a ma3autechlik 
makaynch man mazal men mezian n3ass nass nour nta ounta parcours pieds plus rah 
rak rani sa3a sa7bi sa7eb sahlen sbah sidi tan3ess tou7achnak twelef wata yhfde yhfdek zine''' ))
    print(moroccan_to_arabic('''Fen a 3emo'''))


run_tests()