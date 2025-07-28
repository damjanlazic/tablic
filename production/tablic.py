# make a deck of cards and shuffle it
# deal cards, show hand, deck etc.

from random import randrange
from karta import *

def makeDeck():
    deck=[]
    for suite in ("s","h","d","c"):
        for value in ("2","3","4","5","6","7","8","9","T","J","D","K","A"):
            deck.append(value + suite)
    return(deck)
def shuffle(cards) :
    cards=cards
    for i in range(0,len(cards)) :
        indexToSwitch=randrange(i,len(cards))
        cards[i], cards[indexToSwitch] = cards[indexToSwitch], cards[i]
    return cards

def dealCards(cards,numOfPlayers):
    igrac = [["","","","","",""] for x in range(0,numOfPlayers)]
# pravljeno za tablic tako da se dele po 3 cards za redom svakom igracu, br igraca moze biti 2 ili 4
    first = 0
    last = 3
    for deljenje in range(2):
        for i in range(0,numOfPlayers):
            for k in range(first,last):
                igrac[i][k] = cards.pop(0)
                #
        first = 3
        last = 6           

    return igrac # players

def dealTalon(cards):
    talon = []
    for i in range(4):
        talon.append(cards.pop(len(cards)-1))
    return talon

def testShuffleAndDeal() :
    deck=makeDeck()
    print(deck)
    shuffledDeck=shuffle(deck)
    print(shuffledDeck)
    print("broj karata je: ", len(shuffledDeck))
    hand=dealCards(shuffledDeck,2)
    print(hand)
    print("preostale karte\n", shuffledDeck)
    print("broj preostalih karata je: ", len(shuffledDeck))
    talon = dealTalon(shuffledDeck)
    print("Na talonu su: \t", talon )
    print("preostale karte\n", shuffledDeck)
    print("broj preostalih karata je: ", len(shuffledDeck))

def main():
    deck=makeDeck()
    print(deck)
    shuffledDeck=shuffle(deck)
    print(shuffledDeck)
    print("broj karata je: ", len(shuffledDeck))
#    hand = dealCards(shuffledDeck,2) # posto za sad ne secemo, moze ovo da ide na pocetak daling petlje
#    print(hand)
    print("preostale karte\n", shuffledDeck)
    print("broj preostalih karata je: ", len(shuffledDeck))
    talon = dealTalon(shuffledDeck)
    player1 = Player(1)
    player2 = Player(2)
    Player.talon = CardSet([Card(name) for name in talon])
    for dealing in range(4):
        hand = dealCards(shuffledDeck,2)
        player1.hand = CardSet([Card(c) for c in hand[0]])
        player2.hand = CardSet([Card(c) for c in hand[1]])
        for turn in range(6):
            print("Talon:\n" + Player.talon.printSet() + "\n.................................")

            player1.play(dealing*10 + turn)
            print("Talon:\n")
            print(Player.talon.printSet())
            print("............................\n")
            player2.play(dealing*10 + turn)
            print("Talon:\n")
            print(Player.talon.printSet())
            print("............................\n")
            

    winner = Player.settleScore([player1,player2])
    if winner is not None:
        print("The winner is : {}!\nWith {} points".format(winner.name, winner.points))
    else:
        print("It's a DRAW!!!")


if __name__ == "__main__" :
    main()


