from tablic import *
from computerPlayer import ComputerPlayer
# from karta import *


def main():
    print("Welcome to Tablic!")
    print("This is a game against the computer.")
    human_player_name = input("Enter your name: ")
    deck=makeDeck()
    # print(deck)
    shuffledDeck=shuffle(deck)
    # print(shuffledDeck)
    # print("broj karata je: ", len(shuffledDeck))
#    hand = dealCards(shuffledDeck,2) # posto za sad ne secemo, moze ovo da ide na pocetak daling petlje
#    print(hand)
    # print("preostale karte\n", shuffledDeck)
    # print("broj preostalih karata je: ", len(shuffledDeck))
    talon = dealTalon(shuffledDeck)
    player1 = Player(human_player_name)
    player2 = ComputerPlayer("Computer")
    Player.talon = CardSet([Card(name) for name in talon])
    print("Talon:\n" + Player.talon.printSet() + "\n.................................")
    for dealing in range(4): # 4 dealings for a full game
        hand = dealCards(shuffledDeck,2)
        player1.hand = CardSet([Card(c) for c in hand[0]])
        player2.hand = CardSet([Card(c) for c in hand[1]])

        for turn in range(6): # six cards per turn
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
