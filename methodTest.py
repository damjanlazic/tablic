from karta import *

def eqTest():
    # talon = [Card("Js"),Card("Td"),Card("2d"),Card("2c"),Card("As"),Card("2s"),Card("Ac")]
    talon  = CardSet([Card("As"),Card("Ad"),Card("2d"),Card("2c"),Card("4s"),Card("Ds"),Card("2s"),Card("4c")])
    drugiSet  = CardSet([Card("Ad"),Card("As"),Card("2c"),Card("4s"),Card("2s"),Card("2d"),Card("4c"),Card("Dc")])

    # drugiSet = CardSet([Card("Ks"),Card("8s"),Card("7h"),Card("8h"),Card("9c"),Card("As")])

    igrac1 = Player(1)
    igrac1.hand = CardSet([Card("Ks"),Card("6s"),Card("7h"),Card("Jh"),Card("2h"),Card("Ad")])

    print("talon == drugiSet: ",talon.__eq__(drugiSet))

    print("talon:\n..............")
    talon.printSet()

    print("drugiSet:\n..............")
    drugiSet.printSet()




    # print("\nHand: ")
    # igrac1.printHand()


    # igrac1.play(talon)
    # talon.printSet()
def printTest():
    karta = Card("4c")
    print(karta.printCard())

def loggingTest():
    talon = []
    for k in {"2c","3s","7d","Th","Ds"}:
        talon.append(Card(k))
        logging.debug("loggingTest(): talon.append(Card(k)) - talon: %s", [card.printCard() for card in talon])


def main():
    printTest()
    loggingTest()

main()
