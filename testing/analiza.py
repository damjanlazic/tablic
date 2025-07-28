# ovo je probni computerPlayer.py ako ovo radi onda cemo tamo da ga prebacimo
from karta import *

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.points = 0
        self.taken = 0
        self.newPoints = 0
        self.newTaken = 0
        self.lastTakenInTurn = 0
    
    @staticmethod
    def getCardCombinations(cardPlayed):
        talonValues = []
        cardValueCombinations = []
        for v in Player.talon.values:
            talonValues.append(v)
        doAgain = True
        while doAgain == True:
            for i in range(len(talonValues)+1):
                for subset in combinations(talonValues,i):
                    if sum(subset) == cardPlayed.value:
                            # print("nasao subset: ",list(subset))
                            if subset not in cardValueCombinations: 
                                cardValueCombinations.append(list(subset))
        # ako ima kec, odraditi ovo dva puta, jednom za value=1 a drugi put za value = 11 pa spojiti rezultate
        # problem je sto se na pocetnom talonu moze naci od 1 do 4 keca tako da ovaj problem treba resiti
            if 1 in talonValues:
                for i in range(len(talonValues)):
                    if talonValues[i] == 1:
                        talonValues[i] = 11
                        break   # samo prvom kecu na koga naletimo dacemo vrednost 11, ako ih ima jos ovi ostali ostaju na 1 i to je dovoljno 
                    #     jer ionako dva keca po 11 ne mogu da se kombinuju 
                for i in range(len(talonValues)+1):
                    for subset in combinations(talonValues,i):
                        if sum(subset) == cardPlayed.value:
                            if subset not in cardValueCombinations: 
                                cardValueCombinations.append(list(subset))
       
            doAgain = False
            if cardPlayed.value == 1 :
                cardPlayed.value = 11
                for i in range(len(talonValues)):
                    if talonValues[i] == 11:
                        talonValues[i] = 1

                doAgain = True
# greska? ispitati da li ovo treba da bude pod doAgain petljom i cemu uopste sluzi ako ne? - mozda je samo za logging
        for subset in cardValueCombinations:
            for i in range(len(subset)):
                if subset[i] == 11:
                    subset[i] = 1
        logging.debug("CardValueCombinations for the thrown card: {}, with the available talon:{} are: {}".format(cardPlayed.name,[x for x in Player.talon.names],[i for i in cardValueCombinations]))

        # if Ace was thrown in case it stayed on talon we reset its value back to 1
        if cardPlayed.value == 11 :
            cardPlayed.value = 1

        cardCombinations = []
        
 

# if there are more than one card with the same value we put all those in sameValueCardSet
# so that we can have all possible combinations


        talonCopy = Player.talon.copySet()
        sameValueCards = []
        for value in set(talonCopy.values):
            pendingCardSet = SameValueCardSet(talonCopy.findCardByValue(value))
            # pendingCardSet.printSet()

            if pendingCardSet.numberOfCards > 1:
                sameValueCards.append(pendingCardSet)

# here we just find all the separate combinations with best cards (pointwise) new talon copy for each combination
# later we will expand these combinations so that we get also the less valuable ones
# because combinations can be combined in tablic
        candidate = Card()
        for combination in cardValueCombinations:
            pendingCombination = []
            # talonCopy.copySet(talon)
            talonCopy = Player.talon.copySet() 
            for value in combination:
                for card in talonCopy.cards:
                    if value == card.value:
                        if candidate.points < card.points:
                            candidate = card.copyCard() # old: candidate.copyCard(card)
                            logging.debug("play(self,card): candidate: " + candidate.printCard() )
 
                if candidate.name != None:
                    pendingCombination.append(candidate)
                    logging.debug("play(self,card): pendingCombination.append(candidate) - pendingCombination: %s", [card.printCard() for card in pendingCombination])
                    talonCopy.removeCard(candidate)
                    candidate = Card()

            newCombination = CardSet(pendingCombination)
            pendingCombination = []

            combinationAlreadyExists = False
            for combination in cardCombinations:
                if combination.sameAs(newCombination):
                    combinationAlreadyExists = True

            if combinationAlreadyExists == False:
                cardCombinations.append(newCombination)  

        addedCombination = True
        while addedCombination == True:
            addedCombination = False
            for combination in cardCombinations:
                for valueSet in sameValueCards:
                    overlap = combination.findOverlap(valueSet)
                    if combination.hasOverlap(valueSet) == True:
                        for card in combination.cards:
                            if card.value == valueSet.value:
                                for valueSetCard in valueSet.cards:
                                    newCombFromSameValueCards = combination.copySet()
                                    newCombFromSameValueCards.switchCard(card,valueSetCard)
                                    if newCombFromSameValueCards.sameAs(combination) == False:
                                        # here need to check if the combination is already in cardCombinations 
                                        if newCombFromSameValueCards.isSetInListOfSets(cardCombinations) == False:
                                            cardCombinations.append(newCombFromSameValueCards)
                                            addedCombination = True
                                            logging.debug("play(self,card) - if newCombFromSameValueCards not in cardCombinations - newCombFromSameValueCards: %s", newCombFromSameValueCards.printSet())
              

        combinationJoined = True
        while combinationJoined == True:
            combinationJoined = False
            for index1 in range(len(cardCombinations)):
                for index2 in range(index1 + 1, len(cardCombinations)):
                    if cardCombinations[index1].hasOverlap(cardCombinations[index2]) == False:
                        cardCombinations[index1].addSet(cardCombinations[index2])
                        combinationJoined = True
        return cardCombinations
    
    @staticmethod
    def evaluate_card(cardCombinations):
        if len(cardCombinations) > 0:
            bestSet = CardSet([card for card in cardCombinations[0].cards]) 
            takenAcard = True
            for setOfCards in cardCombinations:
                if bestSet.totalPoints < setOfCards.totalPoints:
                    # bestSet.copySet(setOfCards)
                    bestSet = setOfCards.copySet()
                elif bestSet.totalPoints == setOfCards.totalPoints:
                    if len(bestSet.names) < len(setOfCards.names):
                        # bestSet.copySet(setOfCards)
                        bestSet = setOfCards.copySet()
        else:
            logging.debug("play(self,card) - takenACard = False")
            takenAcard = False
        return bestSet, takenAcard
    
    def play(self, turnCount): 
        cardName = " "
        self.printHand()
        while cardName not in self.hand.names: 
            cardName = input("Pick a card to throw: ")
        cardPlayed = Card(cardName)
        self.hand.removeCard(cardPlayed)

        
        bestSet, takenAcard = self.evaluate_card(self.getCardCombinations(cardPlayed))
        
        if takenAcard == True:
            # add the card that player played with
            self.newPoints += cardPlayed.points
            self.newTaken += 1
            self.lastTakenInTurn = turnCount

            if len(Player.talon.names) == len(bestSet.names): # +1 for tabla
                self.newPoints += 1
                print("TABLA!")

            for card in bestSet.cards:
                Player.talon.removeCard(card)
            self.newPoints += bestSet.totalPoints
            self.newTaken += len(bestSet.names)
            

        else:
            Player.talon.addCard(cardPlayed)

        self.points += self.newPoints
        self.taken += self.newTaken
        self.printStatus()
        self.newPoints = 0
        self.newTaken = 0
