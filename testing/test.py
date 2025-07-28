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
    for p in players:
        p.hand = [Card("0") for i in range(6)] # need to initialise hand to have 6 cards, they will be changed below...

    for deal in range(2):
        for i in range(0,2):
            for k in range(firstCard,lastCard):
                players[i].hand[k] = deckOfCards.pop(0)
                #
        firstCard = 3
        lastCard = 6
    for p in players:
        p.hand = CardSet(p.hand)          
    return players

def dealTalon(deckOfCards):
    talon = []
    for i in range(4):
        talon.append(deckOfCards.pop(len(deckOfCards)-1))
    talonSet = CardSet(talon)
    return talonSet

def lastToTakeTakesRemainingCards(players,talon):
    if players[0].lastTakenInTurn > players[1].lastTakenInTurn:
        taker = 0
    else:
        taker = 1

    for card in talon:
        players[taker].points += card.points
        players[taker].taken += 1
    return players

def threePointsForMostCards(players):
    if players[0].taken > players[1].taken:
        winnerOf3points = 0
    elif players[1].taken > players[0].taken:
        winnerOf3points = 1
    else:
        logging.debug( "threePointsForMostCards(players) nobody wins 3 points, it's a draw: " ) #, players[0].name " has ", players[0].taken, "\n", players[1].name ", has ", players[1].taken )
        return None
    players[winnerOf3points].points += 3
    return players

def theWinner(players):     # compare the points and announce the winner
    if players[0].points > players[1].points:
        print("Player ", players[0].name, " wins!!!")
        players[0].printStatus()
    elif players[0].points < players[1].points:
        print("Player ", players[1].name, " wins!!!")
        players[1].printStatus()
    else:
        print("It's a draw!!!")
        players[0].printStatus()
        players[1].printStatus()


# ovo sad nista ne radi jer su liste kao npr talon pretvorene u objekte klase CardSet a nisu napravljene odgovarajuce izmene, takodje 
# ranije se ta fantomska lista talon ponasala kao globalna promenljiva, a sad izgleda se ponasa normalno tako da nista vise ne radi...


def main():
    d = makeDeck()    
    dshuffled = shuffleDeck(d)


    players = [Player(n) for n in ("Damjan","Najmad")]
    
    talon = dealTalon(dshuffled)
    # print("Cards on the table (talon): ")
    turnCount = 0
    for i in range(4):    # assume we have 2 players only so 4 dealings
        dealCards(dshuffled,players)
        for turn in range(6):
            for p in players:
                print("Cards on the table (talon): ")
                for i in talon.cards:
                    print(i.printCard())
                p.printHand()
                turnCount += 1
                p.play(talon,turnCount)
                p.printStatus()
    if talon != []:
        lastToTakeTakesRemainingCards(players,talon)
    theWinner(players)




            # players[0].play(talon)
            # players[0].printHand()
            # players[0].printStatus()
            
            # print("Cards on the table (talon): ")    
            # for i in talon:
            #     i.printCard()

        # print("Remaining cards: ")
        # for i in dshuffled:
        #     i.printCard()    
# zasto mi ovaj poslednji print stampa izmesani deck ako ne koristim deck1 = deckOfCards.copy()?? trebalo bi da je d - prvobitni spil, a dshuffled - izmesani spil nije mi jasno ovo uopste...
    # print("Original deck again: ")    
    # for i in d:
    #     i.printCard()
        


if __name__ == "__main__" :
    main()