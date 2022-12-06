en = input("entry:  ")


def pig_latin(word):
    voc = 'aouie'
    if word[0] in voc:
        word += 'way'
    else:
        word = word[1:] + word[0] + 'ay'

    return word


functions = pig_latin(en)
print(functions)
