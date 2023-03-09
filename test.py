from karta import *
from random import randrange

def makeDeck():
    deck=[]
    for symbol in ("s","h","d","c"):
        for rank in ("2","3","4","5","6","7","8","9","T","J","D","K","A"):
            card = Card(rank+symbol)
            deck.append(card)
    return(deck)

def shuffleDeck(deck) :
#    deck = deckOfCards
    
    for i in range(0,len(deck)) :
        indexzamene = randrange(i,len(deck))
    #    zamena=deck[indexzamene]
        deck[i], deck[indexzamene] = deck[indexzamene], deck[i]
    return deck

def main():
    print("Original deck: ")
    d = makeDeck()
    for i in d:
        i.printCard()
    print("Shuffled deck: ")    
    dshuffled = shuffleDeck(d)
    for i in dshuffled:
        i.printCard()

# zasto mi ovaj poslednji print stampa izmesani deck?? trebalo bi da je d - prvobitni spil, a dshuffled - izmesani spil nije mi jasno ovo uopste...
    print("Original deck again: ")    
    for i in d:
        i.printCard()
        


if __name__ == "__main__" :
    main()