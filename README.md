This is the first version of tablanet or tablich game made in rudimentary python without any GUI.
It was at first meant as a simple excersize to improve my python skills, but as I tried to make it 
into a real game that one could play it turned out pretty complex. As I worked on it in my free time which 
was sometimes scarce, the project took me a long time to bring to the point where I have the rudimentary 
first version. If you are a python enthusiast or tablich enthusiast, I encourage you to play and dive into 
the code which is all made public here.

To play the game or inspect the final working version of the code go to folder "production" 

for detailed instructions and explanations read aboutTheGame.txt 

- HOW TO SET UP 

You need all the python files from the "production" folder,
copy them to a single folder on a machine where you have python installed
and then run the command (linux terminal):

python3 playAgainstComputer.py

(if you have earlier versions of python it should work too with python playAgainstComputer.py)

- HOW TO PLAY THE GAME  
detailed explanation in production/aboutTheGame.txt

As is mentioned, there is no GUI (for now) so the game is played by typing the names of the cards 
as they appear on the screen. Names are all two character strings with the first character being a 
number 2-9 or A (ace), T (ten), J (jack), D (dame) or K (king), while the second character represents
the suite so it can be c (clubs), s (spades), d (diamonds), h (harts)
For example jack of diamonds is "Jd" while 5 of clubs is "5c"
At the moment it is case sensitive, but if you mistype the name of the card, it will just prompt you to type it again.
When prompted to throw a card you figure out which one would be best and just type the name of that card as shown:
for example if you have 8s and 2c (8 of spades and 2 of clubs) on talon and you have a Td (10 of diamonds) in hand, 
just type Td and press enter, the alghoritm will autamatically work out the best combination(s) to take with the card that you've thrown,
so they will be taken automatically.

The cards are printed out in columns with three rows like this:
Td
10
2
where the first row is the name of the card(Td - ten of diamonds), the second is its numerical value (10), and the third is the number of points (2)

If you want to quit the game without finishing, for now Ctrl+c is the only option.

Enjoy!

