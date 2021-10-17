# This code is by Sid #2281
# Double hashtags implies comment. Single hashtag implies hashed out code.
###########################################

## PT is plain text
PT = input("Enter plain text here: ")


def keygen():
    import random
    c = input("Enter anything to define the key: ")

    if c != '':
        k = input("Enter key")
    else:
        L = []
        for i in PT.split():    L.append(len(i))
        k = str(int(random.random() * (10 ** max(L))))
    return k


def encrypt(k, pt):
    ct = ''
    PT_words = pt.split()
    counter = 0
    for w in PT_words:
        for i in range(len(w)):
            x = ord(w[i])
            ct += chr(x + int(k[i]))
        if counter >= len(k):
            counter = 0

        ct += chr(ord(' ') + int(k[counter]))       ##ct is cypher text
        counter += 1
    return ct


def decrypt(k, ct):
    pt = ''
    counter = 0
    s_counter = 0
    for i in range(len(ct)):
        if s_counter >= len(k):
            s_counter = 0

        if ord(ct[i]) - int(k[s_counter]) == ord(' '):
            counter = 0
            s_counter += 1
            pt += ' '
            continue
        pt += chr(ord(ct[i]) - int(k[counter]))
        counter += 1
    return pt


key = keygen()
print(encrypt(key, PT))
print(key)

CT = input("Enter cipher text: ")
key = input("Enter key: ")
print(decrypt(key, CT))
