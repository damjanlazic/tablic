from itertools import combinations
from copy import deepcopy
import logging

logging.basicConfig(filename='tablicLog.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.DEBUG)
# logging.warning('This will get logged to a file')


class Card:
    def __init__(self, name) -> None:
        self.name = name
        self.value, self.points = self.assignPointsValue()
        logging.debug("Card object created name = {}, value = {}, points = {}".format(self.name,self.value,self.points))
    
    def assignPointsValue(self):
        if self.name == None:
            points = None
            value = None
        else:
            try:
                value = int(self.name[0])
                if self.name == "2c":
                    points = 1
                else:
                    points = 0
            except:
                match self.name[0]:
                    case 'T':
                        value = 10
                        if self.name[1] == "d" :
                            points = 2
                        else:
                            points = 1
                    case 'J':
                        value = 12
                        points = 1
                    case 'D':
                        value = 13
                        points = 1
                    case 'K':
                        value = 14
                        points = 1
                    case 'A':
                        value = 1
                        points = 1
        return value, points
            
    def sameAs(self, other):
        if not hasattr(other, 'name'):
           return False
        logging.debug("Card.sameAs(self,other) \n ...self: name = {}, value = {}, points = {}\n ...other: name = {}, value = {}, points = {}".format(self.name,self.value,self.points,other.name,other.value,other.points))
        logging.debug("Card.sameAs(self,other) returns: {}".format(self.name == other.name))
        return self.name == other.name
    
    def copyCard(self, card):
        self.name = card.name
        self.value = card.value
        self.points = card.points

            
    def printCard(self):
        print(self.name, "\t", self.value, "\t", self.points )

class CardSet:
    def __init__(self, cards) -> None:
        self.cards = [card for card in cards]
        self.names = [card.name for card in cards]
        self.values = [card.value for card in cards]
        self.points = [card.points for card in cards]
        self.totalPoints = sum(self.points)
    
    def copySet(self, otherSet) -> None:
        self.cards = [card for card in otherSet.cards]
        self.names = [name for name in otherSet.names]
        self.values = [value for value in otherSet.values]
        self.points = [points for points in otherSet.points]
        self.totalPoints = sum(self.points)

    def printSet(self): # prints the set so that each column contains name, value, points
        for n in self.names:
            print(n,end = "\t")
        print()
        for v in self.values:
            print(v,end = "\t")
        print()
        for p in self.points:
            print(p,end = "\t")
        print()
        print("total points: ",self.totalPoints)
        # return (' '.join([name for name in self.names]))
    
    def sameAs(self, other):
        logging.debug("CardSet.sameAs(self,other):")
        logging.debug("...self: \t {}".format(' '.join([name for name in self.names])))
        logging.debug("...other:\t {}".format(' '.join([name for name in other.names])))  
        if not hasattr(other, 'totalPoints'):
            logging.debug("...if not hasattr() returns false")
            return False
        if len(self.names) != len(other.names):
            logging.debug("...if different len(names) returns false")
            return False
        for card in other.cards:
            if self.isCardInSet(card) == False:
                logging.debug("...other has card that self has not, card: {} returns false".format(card.name))
                return False
        for card in self.cards:
            if other.isCardInSet(card) == False:
                logging.debug("...self has card that other has not, card: {} returns false".format(card.name))
                return False
        logging.debug("...CardSet.sameAs(self,other) returns: True")
        return True
    
        # for index in range(0,len(self.names)):
        #         if self.names[index] != other.names[index]:
        #              return False
        # return True
# napraviti funkcije za dodavanje jednog Seta drugom i prepoznavanje da li je Set deo drugog Seta    
    def isCardInSet(self,card): # checks if single card is in a Set (used in addCard() which is used in addSet())
        for name in self.names:
            if name == card.name:
                logging.debug("isCardInSet, set: {};\t card: {} returns true".format(' '.join([name for name in self.names]),card.name))
                return True
        logging.debug("isCardInSet, set: {};\t card: {} returns false".format(' '.join([name for name in self.names]),card.name))
        return False
    
    def inSet(self, other): # checks if other is a sub-Set of the self
        for cardName in other.names:
            if cardName not in self.names:
                return False
        return True

   
    def hasOverlap(self,other): # checks if two Sets overlap and returns True or False 
            for name in other.names:
                if name in self.names:
                    return True
            return False
            
    def findOverlap(self,other): # finds the overlapping cards of two sets and returns a CardSet with overlapping cards or returns False if no overlap
        if self.inSet(other):
            return other
        elif other.inSet(self):
            return self
        else:
            overlap = [] # I could use isCardInSet() here but it seems pointless
            for name in other.names:
                if name in self.names:
                    overlap.append(Card(name))
            if overlap == []:
                return False
            else:
                return CardSet(overlap)
    def addCard(self,card): # if card is already in Set returns False (no card added), otherwise it adds the card to Set and retruns True
        if self.isCardInSet(card) == True:
            return False # no card added
        self.cards.append(card)
        self.names.append(card.name)
        self.values.append(card.value)
        self.points.append(card.points)
        self.totalPoints += card.points
        return True # card added
    def removeCard(self, card):
        # if self.isCardInSet(card) == False:
        #     print("Card you are trying to remove is not in the set!")
        #     card.printCard()
        #     return False # card you are trying to remove is not there
        index = 0
        for name in self.names:
            if name == card.name:
                try:
                    self.names.pop(index)
                    self.cards.pop(index)
                    self.values.pop(index)
                    self.points.pop(index)
                    self.totalPoints -= card.points
                    return True
                except:
                    logging.warning("CardSet.removeCard(self,card): self:",self.printSet(),"\t card to be removed: ",card.printCard()," could not be removed")
            index += 1
        logging.warning("CardSet.removeCard(self,card): ",card.printCard()," Card you are trying to remove is not in the set!")
        return False    

    def findCardByValue(self, value):
        cards = []
        for card in self.cards:
            if card.value == value:
                cards.append(card)
        return cards

    def switchCard(self,cardOut,cardIn):
        if self.isCardInSet(cardIn):
            print("No card added one of the two cards to be switched is already in set")
            return False # no card added
        index = 0
        for card in self.cards:
#            card.printCard()
            if card.sameAs(cardOut) == True:
                self.cards[index].copyCard(cardIn)
                self.names[index] = cardIn.name
                self.values[index] = cardIn.value
                self.points[index] = cardIn.points
                self.totalPoints = sum(self.points)
                return True
            index += 1


    def addSet(self,other): # adds the other Set only if there is no overlap (returns True or False whether added or not)
        if self.hasOverlap(other) == False:
            for card in other.cards:
                self.addCard(card)
            return True
        return False

class SameValueCardSet(CardSet):
    def __init__(self, cards) -> None:
        super().__init__(cards)
        self.value = cards[0].value
        self.numberOfCards = len(self.values)
    def printSet(self):
        print("Same card set of cards with value: ", self.value)
        print("Number of cards is : ", self.numberOfCards)
        super().printSet()

class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.hand = CardSet([Card("0") for i in range(6)]) # cards currently in hand / try to initialize it as empty list, than it is supposed to be a list of Card objects
        self.points = 0 # points won by the player during the game, table + shtihovi (T-K+2c) are updated during the game 
        self.taken = 0 # total number of cards won/taken by the player in the end compares with player no2 and +3 points added to the one with larger number of cards taken 
        self.newPoints = 0
        self.newTaken = 0

    def printHand(self):
        print("Player: ", self.name, "\nCards in hand: ", end = "\t")
        for name in self.hand.names:
            print(name, end ="\t")
        print("\n...............")

    def printStatus(self):
        print("player: ", self.name, "\nnew cards taken: ",self.newTaken,"\nnew points collected: ",self.newPoints,"\n", "\ntotal cards taken: ",self.taken,"\ntotal points: ",self.points,"\n")
        

    def play(self,talon):
        cardName = " "
        self.printHand()
        while cardName not in self.hand.names: #handNames:
            cardName = input("Pick a card to throw: ")
        cardPlayed = Card(cardName)
        self.hand.removeCard(cardPlayed)

        talonValues = []
        cardValueCombinations = []
        for v in talon.values:
            talonValues.append(v)
        doAgain = True
        while doAgain == True:
            for i in range(len(talonValues)+1):
                for subset in combinations(talonValues,i):
                    if sum(subset) == cardPlayed.value:
                            print("nasao subset: ",list(subset))
                            if subset not in cardValueCombinations: 
                                cardValueCombinations.append(list(subset))
                                print("ubacio subset: ",list(subset))
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
                            print("nasao subset: ",list(subset))
                            if subset not in cardValueCombinations: 
                                cardValueCombinations.append(list(subset))
                                print("ubacio subset: ",list(subset))        
            doAgain = False
            if cardPlayed.value == 1 :
                cardPlayed.value = 11
                doAgain = True
        print("\nCardValueCombinations: ")
        for subset in cardValueCombinations:
            for i in range(len(subset)):
                if subset[i] == 11:
                    subset[i] = 1
# following 3 lines:  test purposes only
                print(subset[i])
            print(".......end..of..subset.........")
        print("...............the..end....................")

        cardCombinations = []
        
        candidate = Card("0")
        spare = Card("0")

# first time run with just one set of talonCopy needed just for those cases when we have few combinations but also
# cards of same value but different points to chose from
# seemingly I deleted this 


        talonCopy = CardSet([Card("0")])
        talonCopy.copySet(talon)
        sameValueCards = []
        print("set(talonCopy.values)",set(talonCopy.values))
        for value in set(talonCopy.values):
            pendingCardSet = SameValueCardSet(talonCopy.findCardByValue(value))
            pendingCardSet.printSet()

            if pendingCardSet.numberOfCards > 1:
                sameValueCards.append(pendingCardSet)

# 2nd run with a new talon copy for each combination
        candidate = Card("0")
    #    spare = Card("0")
        for combination in cardValueCombinations:
            pendingCombination = []
            talonCopy.copySet(talon) 
            for value in combination:
                index = 0
                for card in talonCopy.cards:
                    if value == card.value:
                        if candidate.points <= card.points:
                        #    spare.copyCard(candidate)
                            candidate.copyCard(card)
                        #    candidateIndex = index
                        # else: 
                        #     spare.copyCard(card)      
                        #     spare.printCard()                 
                    # index += 1

                pendingCombination.append(candidate)
                # print("candidate added: ", candidate.name)
                talonCopy.removeCard(candidate)
                candidate = Card("0")
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
                        print("overlap ima:")
                        overlap.printSet()
                        for card in combination.cards:
                            if card.value == valueSet.value:
                                for valueSetCard in valueSet.cards:
                                    newCombination = CardSet([Card("0")]) # need to recreate this otherwise it will modify the entry in combinations
                                    newCombination.copySet(combination)
                                    newCombination.switchCard(card,valueSetCard)
                                    if newCombination.sameAs(combination) == False:
                                        # here need to check if the combination is already in cardCombinations 
                                        if newCombination not in cardCombinations:
                                            cardCombinations.append(newCombination)
                                            addedCombination = True

        # for combination in cardCombinations:
        #     for sameValueSet in sameValueCards:
        #         overlap = combination.hasOverlap(sameValueSet)
                

        print("Card combinations initial:")        
        for setOfCards in cardCombinations:
            setOfCards.printSet()
            print(".............")

        combinationJoined = True
        while combinationJoined == True:
            combinationJoined = False
            for index1 in range(len(cardCombinations)):
                for index2 in range(index1 + 1, len(cardCombinations)):
                    if cardCombinations[index1].hasOverlap(cardCombinations[index2]) == False:
                        print("cardCombinations[{}] hasOverlap==False with cardCombinations[{}]".format(index1,index2))
                        cardCombinations[index1].printSet()
                        print("..................end of set........................")
                        cardCombinations[index2].printSet()
                        print("..................end of set........................")
                        cardCombinations[index1].addSet(cardCombinations[index2])
                        combinationJoined = True
                        print("cardCombinations[{}] is now: ".format(index1))
                        cardCombinations[index1].printSet()

        print("Card combinations after recombination:")        
        for setOfCards in cardCombinations:
            setOfCards.printSet()
            print(".............")        

        if len(cardCombinations) > 0:
            bestSet = CardSet([card for card in cardCombinations[0].cards]) 
            takenAcard = True
            for setOfCards in cardCombinations:
                if bestSet.totalPoints < setOfCards.totalPoints:
                    bestSet.copySet(setOfCards)
                elif bestSet.totalPoints == setOfCards.totalPoints:
                    if len(bestSet.names) < len(setOfCards.names):
                        bestSet.copySet(setOfCards)
        else:
            print("no card taken") # test purposes only
            takenAcard = False
        
        if takenAcard == True:
            # add the card that player played with
            self.newPoints += cardPlayed.points
            self.newTaken += 1

            print("Best set:")
            bestSet.printSet() 

            talonCopy.copySet(talon)
            print('talonCopy = CardSet(talon)')
            talonCopy.printSet()
            if len(talon.names) == len(bestSet.names): # +1 for tabla
                self.newPoints += 1
                print("TABLA!")

            for card in bestSet.cards:
                talonCopy.removeCard(card)
            self.newPoints += bestSet.totalPoints
            self.newTaken += len(bestSet.names)
            
            # test purposes only
            print('talonCopy after removing the taken cards:')
            talonCopy.printSet()

            talon.copySet(talonCopy)
        else:
            talon.addCard(cardPlayed)
            self.newPoints = 0
            self.newTaken = 0
        self.points += self.newPoints
        self.taken += self.newTaken

        self.printStatus()

        # test purposes only
    #    print("talon u play():\n..............")
        # for c in talon:
        #     c.printCard()
    #    talon.printSet()
