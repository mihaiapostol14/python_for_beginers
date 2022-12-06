with open("words.txt") as file:
    text = file.read()

def separ(text):
    diction = {}
    for i in text:
        if i in diction.keys():
            diction[i]+=1
        else:
            diction.update({i:1})
    print(diction)
separ(text)