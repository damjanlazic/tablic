from tablic import *
from computerPlayer import ComputerPlayer
# from karta import *


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
    player2 = ComputerPlayer(2)
    Player.talon = CardSet([Card(name) for name in talon])
    for dealing in range(1): # normalno je 4
        hand = dealCards(shuffledDeck,2)
        player1.hand = CardSet([Card(c) for c in hand[0]])
        player2.hand = CardSet([Card(c) for c in hand[1]])
        print("Talon:\n" + Player.talon.printSet() + "\n.................................")
        for turn in range(6): # normalno je 6
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
