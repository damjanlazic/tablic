from karta import *

# talon = [Card("Js"),Card("Td"),Card("2d"),Card("2c"),Card("As"),Card("2s"),Card("Ac")]
talon  = CardSet([Card("As"),Card("Ad"),Card("2d"),Card("2c"),Card("4s"),Card("2s"),Card("4c")])


talon.printSet()

# igrac0 = Player("Mrsoje")
# igrac0.hand = CardSet([Card("5h"),Card("2h"),Card("Tc"),Card("Ts"),Card("Jc"),Card("2d")])

igrac1 = Player(1)
igrac1.hand = CardSet([Card("Ks"),Card("6s"),Card("4h"),Card("Jh"),Card("2h"),Card("Ad")])

# for i in range(6):
#     igrac0.play(talon)
#     igrac0.printStatus()
#     for c in talon:
#         print(c.name)


    # igrac1.hand = [Card("Ks"),Card("8s"),Card("7h"),Card("8h"),Card("9c"),Card("6c")]
# igrac1.printHand()
# igrac1.play(talon)


# igrac1.printStatus()
# talon1 = CardSet([Card("Kd"),Card("8c"),Card("7s"),Card("Ad")])

print("talon:\n..............")
talon.printSet()

# drugiSet = CardSet([Card("Ks"),Card("8s"),Card("7h"),Card("8h"),Card("9c"),Card("As")])
# ccombs = [talon, talon1, drugiSet]
# print("ccombs[0].hasOverlap(ccombs[1])",ccombs[0].hasOverlap(ccombs[1]))
# print("ccombs[0].hasOverlap(ccombs[2])",ccombs[0].hasOverlap(ccombs[2]))
# print("ccombs[1].hasOverlap(ccombs[2])",ccombs[1].hasOverlap(ccombs[2]))


# c = Card("Ac")
# if talon.isCardInSet(c) == False:
#     talon.addCard(c)
# d = Card("Ac")
# if talon.isCardInSet(d) == False:
#     talon.addCard(d)
#     print("prrrrrrrrrrrrrrrrc!")
# talon1.addSet(drugiSet)
# print("new talon:\n..............")
# talon1.printSet()
# print("ccombs[0].hasOverlap(ccombs[1])",ccombs[0].hasOverlap(ccombs[1]))
# print("ccombs[0].hasOverlap(ccombs[2])",ccombs[0].hasOverlap(ccombs[2]))
# print("ccombs[1].hasOverlap(ccombs[2])",ccombs[1].hasOverlap(ccombs[2]))






print("\nHand: ")
igrac1.printHand()


    # print("Hand: ")
    # igrac.printHand()
    # print("\nTalon: ")
    # for c in talon:
    #     print(c.name)
igrac1.play(talon)
talon.printSet()
