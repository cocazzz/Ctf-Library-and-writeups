# Cts-Library-and-writeups

Welcome to Catch the santa challenges writeups and source codes.
These challenges were presented in a CTF by h4x0r community which had place in 27th of
December 2020.
Feel free to check the writeups or reuse the challenges source codes in your CTFs
Made with love by **Abdelhak Bouguila** and **abderrahim bouhdida** !
you can check the other part [here](https://github.com/AbderrahimBouhdida/H4X0R-CTS-Writeup)

## Cryptography challenges : ##
**1- Elves City : 300 points**
<br> ♦ description :
<br>WHAT !? people are so strange here, they only count to 5 ?! 
<br> 404 202 440 143 424 443 343 202 203 201 340 402 113 433 201 1000
<br>♣ Solution :
<br>the main idea here is to base 5 decrypt number by number and you directly have the flag
<br>♠ Flag :
<br>```h4x0r{b453_f!v3}```

____________________________________________

<br>**2- Crackable : 600 points**
<br>♦ description :
<br>Can you crack this one + flag txt file + python file
<br>♣ Solution :
<br>Given the encryption and decryption  code, we notice that the encryption is using a key generated randomly
to create the cipher so all we need to do is to find the encryption key . but when observing the encryption
methode we see that ```len(key)==6``` and every character of the key is interacting with one character of the flag
until the key letters are over so the encryption methode uses the first character of it again .
<br>which means the whole encryption process is the following :
<br>for every char in flag : ```encrypt(flag(i),key(i))==cipher(i)```
<br>and the decryption function (which is given in the python code) is:
<br>for every char in cipher : ```decrypt(cipher(i),key(i))==flag(i)```
<br>But here is when the trick comes. the key is random and we have no logical way (as intended) to know it's chars
Although, We know that every flag format in CTS start with ```"h4x0r{"``` .
For that we find ourselves at the situation where :
 <br>```decrypt(cipher(0),key(0))=="h"```
 <br>```decrypt(cipher(1),key(1))=="4"```
 <br>```decrypt(cipher(2),key(2))=="x"```
 <br>```decrypt(cipher(3),key(3))=="0"```
 <br>```decrypt(cipher(4),key(4))=="r"```
 <br>```decrypt(cipher(5),key(5))=="{"```
<br>
<br>And based on that , finding the key becomes a piece of cake. and once we find the key we can pass it to the decrypt
function with the flag and abra kadabra, the flag is yours !
(you can find the solution code at the challenge repository)
<br>♠ Flag :
<br>```h4x0r{SANt4_M0re_L1ke_SATAN!}```
______________________________________
<br>**3- Math : 700 points**
<br>♦ description :
<br>Connect with: ```nc h4xor.tech 1022```
<br>mathematical sequences are so much the hardest to solve, that's why it is
always used in cryptography and ciphering. for example by just transforming 
an ord() of a plain text by a sequence makes it kind of impossible to crack ...
<br>7 - 20 - 47 - 94 - 197 - ... + flag cipher
<br>♣ Solution :
<br>This on is nothing but a math problem. and all we have to do is to find the
mathematical sequence used for the encryption :
<br>Given that N1 = 7 , N2=20, N3= 47, ...
<br>let's try to solve it by playing with an X variable.
<br>the massive increase of the iterations will certainly lead our thoughts to
power the variable X. when we try to X² everytime and the result is still very
far of what we find. so we try to Xⁿ with other integers and we start with n=3.
the result of cubing the X leads us to : A1=1, A2=8, A3=27, ... but when we try
to power by 4 the results go higher than the mathematical sequence ones. so We
Stick with power 3. if we try to find the difference between the mathematical 
sequence result and the cubes result we will find the following :
<br>```N1-A1=6=3x2=(1+1)x(1+2)```
<br>```N2-A2=12=3x4=(2+1)x(2+2)```
<br>```N3-A3=20=4x5=(3+1)x(3+2)```
<br>```N4-A4=30=5x6=(4+1)x(4+2)```
<br>TADA ! the sequence is : ```N(X)=(X^3)+(X+1)x(X+2)```
<br>Now the only thing we have to do is to write the script that decrypts based on
this mathematical sequence. (you can find the code in the challenge repository)
<br>♠ Flag :
<br>```h4x0r{Xm4S_Maths_Are_L0ve}```

## WEB challenges : ##
**1- Pokemaniacs : 500 points**
<br> ♦ description :
<br> only IP and port given
<br> ♣ Solution :
<br> This web application will ask us to give a valide pokemon name and will give us a certification as that mentionned pokemon fan
<br> ![1](https://user-images.githubusercontent.com/61564815/103538133-f1472f80-4e95-11eb-918c-100aa249a270.png)
<br> This web application can be a victime of [HTML injection](https://www.acunetix.com/vulnerabilities/web/html-injection/)
<br> We can discover that by passing any html tag in the post request or by just passing it in the input box and we can see that tag effect in the resulted pdf
<br> So if we pass ```<iframe src='flag.txt'></iframe>``` in the input box, the flag will show up in the downloaded PDF !
<br> ![2](https://user-images.githubusercontent.com/61564815/103539386-41bf8c80-4e98-11eb-8219-bf12fe63352e.png)
<br>♠ Flag :
<br> h4x0r{1_WaNNA_B3.the_VERY_B3st}
____________________________________________
<br> **2- Kurisumasu : 700 points**
<br> ♦ description :
<br> IP and port given
<br> hint: dirbuster is allowed, use it !
<br> ♣ Solution :
<br> Once we open this web application, we see a Cute interface with stuff written in japanese. We do not care we are here to hack stuff.
<br>![3](https://user-images.githubusercontent.com/61564815/103540473-07ef8580-4e9a-11eb-93f7-eee89233d8ba.png)
<br> Since the hint says Dirb is allowed, so that's what we gonna try first. and we get a 200 on /backup. this directory will return a zip file which contains the architecture of this flask application . the first thing we see that it has a txt file named "so_secret_creds_file.txt" and a directory that will lead us to a secret login interface on "/super_secret_admin" that we can discover in the python file. 
<br> ![4](https://user-images.githubusercontent.com/61564815/103541009-fe1a5200-4e9a-11eb-9bd9-4f39b06a328a.png)
<br> the first thing we want to do is to reach that password file in the system. we can't just access to it in the browser since the flask does not allow that so we need to figue out a way to do it. 
<br> Let's take a look at that post request we have in the application. We will be using burp Suit.
<br> Do we see an LFI ? that's exactly what we will be using !
![5](https://user-images.githubusercontent.com/61564815/103541616-00c97700-4e9c-11eb-9b3c-9b2b3361226d.png)
<br> now we just have to adjust the page parameter in the request and get the password file. ```page=so_secret_creds_file.txt``` and Gotcha!
<br> ```username : kanako
password : SantaSanSanS4N<3 ```
<br> Now by just connecting in that secret login we can get the flag !
<br>♠ Flag :
<br> h4x0r{I_Kn0W_This_Song_FROM_0SU!}
_______________________________________________
<br> **3- File HUB : 850 points**
<br> ♦ description :
<br> IP and port given
<br> hint: os.system('touch ./files/' + str(userid))
<br> ♣ Solution :
<br> Filehub is the hardest challenge in Capture The Santa and needs a little bit of thinking. the first thing we need to discover is how the web application works. 
<br> the File hub : 
<br> 1- sets a random guest username to any new connection
<br> 2- The user gets to create a file in the system with it's username
<br> 3- The user can check if he has a file in the system and reads its content.
<br> ![6](https://user-images.githubusercontent.com/61564815/103544092-d4175e80-4e9f-11eb-99e6-b2310b54834a.png)
<br> The first step we must do is figuring out where and how the app is setting the username. burpsuit it is !
<br> This application is using a session cookie as seen in the photo. and we get it right by decrypting it with base 64 !
<br>![image](https://user-images.githubusercontent.com/61564815/103544425-63247680-4ea0-11eb-9dd3-f8d165829922.png)
<br> <h4> PART 1 </h4>
<br> Now we know that we have to messup with this session cookie ! but we are sure that since it is a flask app again. we have to crack the secret key by using ```Flask-unsign -c -u <token> ``` command. and the secret key is "secret-key-goes-here" lol . 
<br> now that we have the secret key , one of the ideas to create a new token is to create a flask application with the same secret key and set the user string the way we like.
<br> example of a python code :
<br>
``` py
from flask import Flask, session, redirect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
@app.route('/')
def index():
    session['user'] = "put your username here"
    return session.get('user')

app.run(host='127.0.0.1', port=8000) 
``` 
<br> run this flask app and get the needed token !
<br> <h4> PART 2 </h4>
<br> Now that the token is under controle . it's time to check the hint that says ```os.system('touch ./files/' + str(userid))```. this hint tells how the file is created in the system . ```os.system()``` in python is used to run internal commands and in our case we will be running ``` touch ./files/username ``` and touch is a linux command used to create files. and this one is a 100% used in the /create as the http method we can discover when we intercept that create button :
<br>![image](https://user-images.githubusercontent.com/61564815/103547652-fbbcf580-4ea4-11eb-9686-82de8ec8cebd.png)
<br> the trick here is to transform into a usefull RCE ! there is much to do here but on of the idea is to set the user as ``` user= "<username> & cat ./flag > ./file/username" ``` so the running command will be ``` touch ./files/<username> & cat ./flag > ./file/username ``` and abra kadabra. now the flag is in our file in the system !
<br><br> ![image](https://user-images.githubusercontent.com/61564815/103547459-b4cf0000-4ea4-11eb-8206-0e34e3209f2e.png)
<br><br> ![image](https://user-images.githubusercontent.com/61564815/103548066-843b9600-4ea5-11eb-90eb-e07e0a788994.png)
<br><br> <h4> PART 3 </h4>
<br> now that our file system contains the flag, all we have to do is to read it. but again when we refresh the page we are assigned a new random guest username again. So we need to have that user "pwner" again and we are going to use our python script again. once we set the final token , we create a post request of the /show that we discover when intercepting the show file button. and finally, FILE HUB is owned !
<br><br>![image](https://user-images.githubusercontent.com/61564815/103548777-94a04080-4ea6-11eb-9a89-b6f45c4a2cb3.png)
<br>♠ Flag :
<br> h4x0r{Y0u_4r3_br34tH74k!ng}

## Reverse challenges : ##
<br> **3- 1000 Wishes : 850 points**
<br> ♦ description :
<br> merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! merry xmas ! ...
<br> ♣ Solution :
<br> This challenge is unintendedly solveable by [pyinstaller decompiler](https://awesomeopensource.com/project/extremecoders-re/pyinstxtractor) called pyinstxtractor.
<br>♠ Flag :
<br> h4x0r{1000_wiShes_2_All_your_Dish3s!}
