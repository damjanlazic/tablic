from karta import *
from random import randrange

def makeDeck():
    deck=[]
    for symbol in ("s","h","d","c"):
        for rank in ("2","3","4","5","6","7","8","9","T","J","D","K","A"):
            card = Card(rank+symbol)
            deck.append(card)
    return(deck)

def shuffleDeck(deckOfCards) :
    deck1 = deckOfCards.copy() # if you use deckOfCards below or try deck1 = deckOfCards this function will also change the original deck in the main functions
    
    for i in range(0,len(deck1)) :
        indexzamene = randrange(i,len(deck1))
        deck1[i], deck1[indexzamene] = deck1[indexzamene], deck1[i]
    return deck1

def dealCards(deckOfCards,players):
    firstCard = 0
    lastCard = 3
    for deljenje in range(2):
        for i in range(0,2):
            for k in range(firstCard,lastCard):
                players[i].hand[k] = deckOfCards.pop(0)
                #
        firstCard = 3
        lastCard = 6           
    return players

def dealTalon(deckOfCards):
    talon = []
    for i in range(4):
        talon.append(deckOfCards.pop(len(deckOfCards)-1))
    return talon


def main():
    # print("Original deck: ")
    d = makeDeck()
    # for i in d:
    #     i.printCard()
    # print("Shuffled deck: ")    
    dshuffled = shuffleDeck(d)
    # for i in dshuffled:
    #     i.printCard()

    players = [Player(n) for n in range(2)]
    dealCards(dshuffled,players)
    for p in players:
        p.printHand()

    # print("Remaining cards: ")
    # for i in dshuffled:
    #     i.printCard()    

    talon = dealTalon(dshuffled)
    print("Cards on the table (talon): ")
    for i in talon:
        i.printCard()
    
    # print("Remaining cards: ")
    # for i in dshuffled:
    #     i.printCard()

    players[0].play(talon)
    players[0].printHand()
    players[0].printStatus()
    
    print("Cards on the table (talon): ")    
    for i in talon:
        i.printCard()
# zasto mi ovaj poslednji print stampa izmesani deck ako ne koristim deck1 = deckOfCards.copy()?? trebalo bi da je d - prvobitni spil, a dshuffled - izmesani spil nije mi jasno ovo uopste...
    # print("Original deck again: ")    
    # for i in d:
    #     i.printCard()
        


if __name__ == "__main__" :
    main()