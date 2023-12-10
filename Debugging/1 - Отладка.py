def add_underscores(word):
    new_word = '_'
    #
    for pines in word:
        new_word =new_word + pines+'_'
    return new_word

phrase = 'hello'
print(add_underscores(phrase))