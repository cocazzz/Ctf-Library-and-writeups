#key must be the length of the flag header
#in our case, the header is "h4x0r{" nad the length is 6
#in encryption function we see that the random number is between 1 and 50

KEY=""
S="put cipher here"

for i in range(50) :

    K=chr(ord(S[0])-i)
    if (K == "h") :
        KEY=KEY+chr(i)
        break


for i in range(50) :

    K=chr(ord(S[1])-i)
    if (K == "4") :
        KEY=KEY+chr(i)
        break

for i in range(50) :

    K=chr(ord(S[2])-i)
    if (K == "x") :
        KEY=KEY+chr(i)
        break

for i in range(50) :

    K=chr(ord(S[3])-i)
    if (K == "0") :
        KEY=KEY+chr(i)
        break

for i in range(50) :

    K=chr(ord(S[4])-i)
    if (K == "r") :
        KEY=KEY+chr(i)
        break

for i in range(50) :

    K=chr(ord(S[5])-i)
    if (K == "{") :
        KEY=KEY+chr(i)
        break


print (KEY)
