from karta import *

# talonN = [Card("Js"),Card("Td"),Card("2d"),Card("2c"),Card("As"),Card("2s"),Card("Ac")]
talonN  = [Card("As"),Card("2c"),Card("4s"),Card("2s"),Card("4c")] #,Card("9c")]
# talonN = [Card("8s"),Card("2s"),Card("2c"),Card("Ah")] # bug za keca kad nece da nosi 8+2+1 =11

# igrac0 = Player("Mrsoje")
# igrac0.hand = CardSet([Card("5h"),Card("2h"),Card("Tc"),Card("Ts"),Card("Jc"),Card("2d")])

igrac1 = Player(1)
igrac1.hand = CardSet([Card("Ks"),Card("6s"),Card("4h"),Card("Jh"),Card("2h"),Card("Ad")]) # As
igrac2 = Player(2)
igrac2.hand = CardSet([Card("5h"),Card("2d"),Card("Td"),Card("Ts"),Card("Qc"),Card("3d")])
Player.talon = CardSet(talonN)

print("Talon:\n")
print(Player.talon.printSet())
print("............................\n")

print("\nHand: ")
igrac1.printHand()


igrac1.play(0)
print("Talon:\n")
print(Player.talon.printSet())
print("\nigrac1 - Hand: ")
igrac1.printHand()

igrac2.play(0)
print("Talon:\n")
print(Player.talon.printSet())
print("\nigrac2 - Hand: ")
igrac2.printHand()
