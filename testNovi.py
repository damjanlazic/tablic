from karta import *

# talon = [Card("Js"),Card("Td"),Card("2d"),Card("2c"),Card("As"),Card("2s"),Card("Ac")]
talon  = CardSet([Card("As"),Card("Ad"),Card("2d"),Card("2c"),Card("4s"),Card("2s"),Card("4c")])

# for c in talon:
#     print(c.name)
talon.printSet()

igrac0 = Player("Mrsoje")
igrac0.hand = CardSet([Card("5h"),Card("2h"),Card("Tc"),Card("Ts"),Card("Jc"),Card("2d")])
igrac1 = Player(1)
igrac1.hand = CardSet([Card("Ks"),Card("6s"),Card("7h"),Card("Jh"),Card("2h"),Card("Ad")])
# for i in range(6):
#     igrac0.play(talon)
#     igrac0.printStatus()
#     for c in talon:
#         print(c.name)


    # igrac1.hand = [Card("Ks"),Card("8s"),Card("7h"),Card("8h"),Card("9c"),Card("6c")]
# igrac1.printHand()
igrac1.play(talon)


# igrac1.printStatus()

print("talon:\n..............")
# for c in talon:
#     c.printCard()
talon.printSet()
# print("\nHand: ")
# igrac1.printHand()


    # print("Hand: ")
    # igrac.printHand()
    # print("\nTalon: ")
    # for c in talon:
    #     print(c.name)
igrac1.play(talon)
