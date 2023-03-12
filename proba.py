from karta import *

talon = [Card("Ac"),Card("2d"),Card("5c"),Card("6s")]
for c in talon:
    print(c.name)

igrac = Player(1)
igrac.hand = [Card("2c"),Card("7d"),Card("4c"),Card("Ks"),Card("5s"),Card("Ad")]
igrac.play(talon)

igrac.printStatus()
# print("Hand: ")
# igrac.printHand()
print("\nTalon: ")
for c in talon:
    print(c.name)

