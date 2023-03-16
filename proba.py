from karta import *

talon = [Card("Js"),Card("Td"),Card("2s"),Card("2c"),Card("4s")]
for c in talon:
    print(c.name)

igrac0 = Player(1)
igrac0.hand = [Card("3h"),Card("2h"),Card("Tc"),Card("Ts"),Card("Jc"),Card("2d")]
igrac1 = Player(1)
igrac1.hand = [Card("Ks"),Card("8s"),Card("7h"),Card("8h"),Card("9c"),Card("Ac")]
for i in range(6):
    igrac0.play(talon)
    igrac0.printStatus()
    for c in talon:
        print(c.name)


    # igrac1.hand = [Card("Ks"),Card("8s"),Card("7h"),Card("8h"),Card("9c"),Card("6c")]

    igrac1.play(talon)

    igrac1.printStatus()
    # print("Hand: ")
    # igrac.printHand()
    print("\nTalon: ")
    for c in talon:
        print(c.name)

