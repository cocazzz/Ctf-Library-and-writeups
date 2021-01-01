import random


def get_key () :
    s=""
    a=random.randint(10,50)
    for i in range(6) :
        s= s + chr(a ^ i)
    return (s)

def encrypt (flag,S) :
    enc=""
    for i in range(len(flag)) :
        A= S[i%6]
        enc=enc+chr(ord(flag[i])+ord(A))
    return enc


flag="put flag here"


AA=get_key()
encryptedS=encrypt(flag, AA)
message = "HO HO HO! SANTA DOES CIPHERS ! \n"

print(message)
print(encryptedS)
