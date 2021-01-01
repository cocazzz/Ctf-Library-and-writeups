#encryption
flag="put your flag here"
def encrypt (flag) :
	S=[]
	for i in range(len(flag)):
		S.append( ord(flag[i]) **3 + ( ord(flag[i])+1 ) *( ord(flag[i]) +2) )
	return (S)

message ='''mathematical sequences are so much the hardest to solve, that's why it is
always used in cryptography and ciphering. for example by just transforming 
an ord() of a plain text by a sequence makes it kind of impossible to crack ...
7 - 20 - 47 - 94 - 197 - ... \n

#display
print(message)
print(str(encrypt(flag)))
