message = input("Enter words:\n")

def get_cipher_text(text):
    translated = ''  # cipher text is stored in this variable
    i = len(text) - 1

    while i >= 0:
        translated = translated + text[i]
        i = i - 1

    return translated
print('this is word cipher :>>',get_cipher_text(message))
