from karta import *

# talon = [Card("Js"),Card("Td"),Card("2d"),Card("2c"),Card("As"),Card("2s"),Card("Ac")]
talon  = [Card("As"),Card("Ad"),Card("2d"),Card("2c"),Card("4s"),Card("2s"),Card("4c")]


# igrac0 = Player("Mrsoje")
# igrac0.hand = CardSet([Card("5h"),Card("2h"),Card("Tc"),Card("Ts"),Card("Jc"),Card("2d")])

igrac1 = Player(1)
igrac1.hand = CardSet([Card("Ks"),Card("6s"),Card("4h"),Card("Jh"),Card("2h"),Card("Ad")])
igrac2 = Player(2)
Player.talon = CardSet(talon)

print("Talon:\n")
print(Player.talon.printSet())

print("\nHand: ")
igrac1.printHand()

# greska je u play metodu, verovatno negde se talon koristi na stari nacin ili tako nesto...

igrac1.play(0)
print("Talon:\n")
print(Player.talon.printSet())
print("\nigrac1 - Hand: ")
igrac1.printHand()

# igrac2.play(talon,0)
