# Converte a letter to its substitute
def letter_to_substitute(l):
    if l == '7': return 'h'
    elif l == '9': return 'q'
    else : return l

# Converte a word to its substitute
def word_to_substitute(word):
    return ''.join(list(map(lambda x:letter_to_substitute(x), word)))

# Temporary function to test
def run_tests():
    print(word_to_substitute('7alwa'))
    print(word_to_substitute('9o9o'))

run_tests()