import string
KEY = 5

alpha = string.ascii_lowercase + "0123456789/ "

def char_encrypt(key, string):
    cipher = ""
    for letter in string:
        if letter in string:
            new_position = ( alpha.index(letter) + key ) % len(alpha)
            cipher += alpha[new_position]
        else :
            cipher += letter
    return cipher

def char_decrypt(key, string):
    cipher = ""
    for letter in string:
        if letter in string:
            new_position = ( alpha.index(letter) - key ) % len(alpha)
            cipher += alpha[new_position]
        else :
            cipher += letter
    return cipher

