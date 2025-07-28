from tablic import *

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

def copyTest():
    talon  = [Card("As"),Card("Ad"),Card("2d"),Card("2c"),Card("4s"),Card("2s"),Card("4c")]
    player1 = Player("Zia")
    Player.talon = CardSet(talon)
    print("Player.talon:\n", Player.talon.printSet())
    talonCopy = Player.talon.copySet()
    print("talonCopy:\n", talonCopy.printSet())
    talonCopy.removeCard(Card("As"))
    Player.talon.removeCard(Card("2s"))
    print("Nakon izbacivanja karte As iz talonCopy-ja: i 2s iz Player.talon-a:\n")
    print("Player.talon:\n", Player.talon.printSet())
    print("talonCopy:\n", talonCopy.printSet())

def gameTestShort():
    deck=makeDeck()
    print(deck)
    shuffledDeck=shuffle(deck)
    print(shuffledDeck)
    print("broj karata je: ", len(shuffledDeck))
#    hand = dealCards(shuffledDeck,2) # posto za sad ne secemo, moze ovo da ide na pocetak daling petlje
#     print(hand)
    print("preostale karte\n", shuffledDeck)
    print("broj preostalih karata je: ", len(shuffledDeck))
    talon = dealTalon(shuffledDeck)
    player1 = Player(1)
    player2 = Player(2)
    Player.talon = CardSet([Card(name) for name in talon])
    for dealing in range(1):
        hand = dealCards(shuffledDeck,2)
        player1.hand = CardSet([Card(c) for c in hand[0]])
        player2.hand = CardSet([Card(c) for c in hand[1]])
        for turn in range(2):
            print("Talon:\n" + Player.talon.printSet() + "\n.................................")

            player1.play(dealing*10 + turn)
            print("Talon:\n")
            print(Player.talon.printSet())
            print("............................\n")
            player2.play(dealing*10 + turn)
            print("Talon:\n")
            print(Player.talon.printSet())
            print("............................\n")
            
    playersList = [player1,player2]
    winner = Player.settleScore(playersList) # kaze takes one positional argument but two were given... greska
    if winner is not None:
        print("The winner is : {}!\nWith {} points".format(winner.name, winner.points))
    else:
        print("It's a DRAW!!!")


def main():
    # printTest()
    # loggingTest()
    # copyTest()
    gameTestShort()
main()
