from karta import *


# # talon = [Card("Js"),Card("Td"),Card("2d"),Card("2c"),Card("As"),Card("2s"),Card("Ac")]
# talon  = CardSet([Card("As"),Card("Ad"),Card("2d"),Card("2c"),Card("4s"),Card("Ds"),Card("2s"),Card("4c")])
# drugiSet  = CardSet([Card("Ad"),Card("As"),Card("2c"),Card("4s"),Card("2s"),Card("2d"),Card("4c"),Card("Dc")])

# # drugiSet = CardSet([Card("Ks"),Card("8s"),Card("7h"),Card("8h"),Card("9c"),Card("As")])

# igrac1 = Player(1)
# igrac1.hand = CardSet([Card("Ks"),Card("6s"),Card("7h"),Card("Jh"),Card("2h"),Card("Ad")])

# print("talon == drugiSet: ",talon.__eq__(drugiSet))

# print("talon:\n..............")
# talon.printSet()

# print("drugiSet:\n..............")
# drugiSet.printSet()
aCard = Card(None)

try:
    if aCard.value >= 0 :
        print("value= ",aCard.value)
except:
    aCard = Card("As")
    aCard.printCard()
