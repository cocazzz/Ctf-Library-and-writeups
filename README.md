# Cts-Library-and-writeups

Welcome to Catch the santa challenges write-ups and source codes.
These challenges were presented in a CTF by h4x0r community which had place in 27th of
December 2020.
Feel free to check the write-ups or reuse the challenges source codes in your CTFs
Made with love by Abdelhak Bouguila and h4x0r team !

# Cryptography challenges :

1- Elves City : 300 points
<br> ♦ description :
WHAT !? people are so strange here, they only count to 5 ?! 
404 202 440 143 424 443 343 202 203 201 340 402 113 433 201 1000
♣ Solution :
the main idea here is to base 5 decrypt number by number and you directly have the flag
♠ Flag :
h4x0r{b453_f!v3}

2- Crackable :
♦ description :
Can you crack this one + flag txt file + python file
♣ Solution :
Given the encryption and decryption  code, we notice that the encryption is using a key generated randomly
to create the cipher so all we need to do is to find the encryption key . but when observing the encryption
methode we see that len(key)==6 and every character of the key is interacting with one character of the flag
until the key letters are over so the encryption methode uses the first character of it again .
which means the whole encryption process is the following :
for every char in flag : encrypt(flag(i),key(i))==cipher(i)
and the decryption function (which is given in the python code) is:
for every char in cipher : decrypt(cipher(i),key(i))==flag(i)
But here is when the trick comes. the key is random and we have no logical way (as intended) to know it's chars
Although, We know that every flag format in CTS start with "h4x0r{" .
For that we find ourselves at the situation where :
 decrypt(cipher(0),key(0))=="h"
 decrypt(cipher(1),key(1))=="4"
 decrypt(cipher(2),key(2))=="x"
 decrypt(cipher(3),key(3))=="0"
 decrypt(cipher(4),key(4))=="r"
 decrypt(cipher(5),key(5))=="{"

And based on that , finding the key becomes a piece of cake. and once we find the key we can pass it to the decrypt
function with the flag and abra kadabra, the flag is yours !
(you can find the solution code at the challenge repository)
♠ Flag :
h4x0r{SANt4_M0re_L1ke_SATAN!}

3- Math :
♦ description :
Connect with: nc h4xor.tech 1022
_________________________________
mathematical sequences are so much the hardest to solve, that's why it is
always used in cryptography and ciphering. for example by just transforming 
an ord() of a plain text by a sequence makes it kind of impossible to crack ...
7 - 20 - 47 - 94 - 197 - ... + flag cipher
♣ Solution :
This on is nothing but a math problem. and all we have to do is to find the
mathematical sequence used for the encryption :
Given that N1 = 7 , N2=20, N3= 47, ...
let's try to solve it by playing with an X variable.
the massive increase of the iterations will certainly lead our thoughts to
power the variable X. when we try to X² everytime and the result is still very
far of what we find. so we try to Xⁿ with other integers and we start with n=3.
the result of cubing the X leads us to : A1=1, A2=8, A3=27, ... but when we try
to power by 4 the results go higher than the mathematical sequence ones. so We
Stick with power 3. if we try to find the difference between the mathematical 
sequence result and the cubes result we will find the following :
N1-A1=6=3x2=(1+1)x(1+2)
N2-A2=12=3x4=(2+1)x(2+2)
N3-A3=20=4x5=(3+1)x(3+2)
N4-A4=30=5x6=(4+1)x(4+2)
TADA ! the sequence is : N(X)=(X^3)+(X+1)x(X+2)
Now the only thing we have to do is to write the script that decrypts based on
this mathematical sequence. (you can find the code in the challenge repository)
♠ Flag :
h4x0r{Xm4S_Maths_Are_L0ve}


