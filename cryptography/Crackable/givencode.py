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

def decrypt (enc, S) :
    flag =""
    for i in range(len(enc)) :
        A= S[i%6]
        flag = flag + chr(ord(enc[i])-ord(A))
    return flag
