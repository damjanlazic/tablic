
# no errors in operation - peculiar behavior with inheritance sameValueCardSet variables of child class object not recognized by the printSet overriden child class method

from itertools import combinations
from copy import deepcopy
import logging

logging.basicConfig(filename='tablicLog.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s - %(lineno)d')
# logging.basicConfig(level=logging.DEBUG)
# logging.warning('This will get logged to a file')
# in format to add time: %(asctime)s

class Card:
    def __init__(self, name=None) -> None:
        self.name = name if name else None
        self.value, self.points = self.assignPointsValue()
        logging.debug("Card object created name = {}, value = {}, points = {}".format(self.name,self.value,self.points))
    
    def assignPointsValue(self):
        if self.name == None:
            points = -1
            value = -1
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
                    case 'Q':
                        value = 13
                        points = 1
                    case 'K':
                        value = 14
                        points = 1
                    case 'A':
                        value = 1
                        points = 1
                    case _ :
                        print("Invalid Card Name!!!", self.name)
        return value, points
            
    def sameAs(self, other):
        if not hasattr(other, 'name'):
           return False
        logging.debug("Card.sameAs(self,other) \n ...self: name = {}, value = {}, points = {}\n ...other: name = {}, value = {}, points = {}".format(self.name,self.value,self.points,other.name,other.value,other.points))
        logging.debug("Card.sameAs(self,other) returns: {}".format(self.name == other.name))
        return self.name == other.name
    

    def copyCard(self):
        return Card(self.name)
    
            
    def printCard(self):
        return f"{self.name} | {self.value} | {self.points}"


class CardSet:
    def __init__(self, cards) -> None:
        self.cards = cards if cards else [] # [card for card in cards] #  
        self.names = [card.name for card in cards]
        self.values = [card.value for card in cards]
        self.points = [card.points for card in cards]
        # try:
        self.totalPoints = sum(self.points)
        logging.debug("CardSet __init__\n" + self.printSet())
        if -1 in self.points:
            logging.warning("CardSet init - set with card(s) of None type created!")


    def copySet(self): # -> CardSet:
        cards = [Card(name) for name in self.names]
        return CardSet(cards)

    def printSet(self): # prints the set so that each column contains name, value, points
        printString = ""
        for n in self.names:
            if n == None:
                printString += "None\t"
            else:
                printString += n + "\t" # print(n,end = "\t")
        printString += "\n" # print()
        for v in self.values:
            printString += str(v) + "\t" # print(v,end = "\t")
        printString += "\n" # print()
        for p in self.points:
            printString += str(p) + "\t" # print(p,end = "\t")
        printString += "\n" # print()
        printString += "total points: " + str(self.totalPoints) # print("total points: ",self.totalPoints)
        return printString
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
    

    def isSetInListOfSets(self,listOfSets):
        for set in listOfSets:
            if self.sameAs(set) == True:
                return True
        return False

    def isCardInSet(self,card): # checks if single card is in a Set (used in addCard() which is used in addSet())
        if card is None:
            logging.warning("isCardInSet, set: {};\t card: None returns false - tried to check for card of type None".format(' '.join([name for name in self.names])))
            return False
        for name in self.names:
            if name == card.name:
                logging.debug("isCardInSet, set: {};\t card: {} returns true".format(' '.join([name for name in self.names]),card.name))
                return True
        logging.debug("isCardInSet, set: {};\t card: {} returns false".format(' '.join([name for name in self.names]),card.name))
        return False

# this is not used I think... consider deleting this...    
    def inSet(self, other): # checks if other is a sub-Set of the self
        for cardName in other.names:
            if cardName not in self.names:
                return False
        return True

   
    def hasOverlap(self,other): # checks if two Sets overlap and returns True or False 
        if self is None or other is None or not self.cards or not other.cards:
            logging.warning("hasOverlap, set1: {};\t set2: {} returns true because one set is None".format(' '.join([name for name in self.names]),' '.join([name for name in other.names])))
            return True # returning true since one set is None and we don't want to deal with it
        else:
            for name in other.names:
                if name in self.names:
                    return True
            logging.debug("hasOverlap, set1: {};\t set2: {} returns false".format(' '.join([name for name in self.names]),' '.join([name for name in other.names])))
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
        if self.isCardInSet(None):
            for anyCard in self.cards:
                if anyCard.name == None:
                    self.removeCard(None)
        self.cards.append(card)
        self.names.append(card.name)
        self.values.append(card.value)
        self.points.append(card.points)
        self.totalPoints += card.points
        return True # card added
    def removeCard(self, card):
        index = 0
        for name in self.names:
            if name == card.name:
                try:
                    self.names.pop(index)
                    self.cards.pop(index)
                    self.values.pop(index)
                    self.points.pop(index)
                    self.totalPoints -= card.points
                    logging.debug("CardSet.removeCard(self,card): " + card.printCard() + " Card removed!")
                    return True
                except:
                    logging.warning("CardSet.removeCard(self,card): self:" + self.printSet() + "\t card to be removed: " + card.printCard() + " could not be removed")
            index += 1
        logging.warning("CardSet.removeCard(self,card): " + card.printCard() + " Card you are trying to remove is not in the set!")
        return False    

    def findCardByValue(self, value):
        cards = []
        for card in self.cards:
            if card.value == value:
                cards.append(card)
        return cards

    def switchCard(self,cardOut,cardIn):
        if self.isCardInSet(cardIn):
            logging.warning("switchCard(self,card): " + cardIn.printCard() + " No card added one of the two cards to be switched is already in set")
            return False # no card added
        index = 0
        for card in self.cards:
            if card.sameAs(cardOut) == True:
                self.cards[index] = cardIn.copyCard() # old use: self.cards[index].copyCard(cardIn)
                self.names[index] = cardIn.name
                self.values[index] = cardIn.value
                self.points[index] = cardIn.points
                self.totalPoints = sum(self.points)
                logging.debug("switchCard(self,card): cardIn: " + cardIn.printCard() + " switched in stead of cardOut: " + cardOut.printCard() )
                return True
            index += 1


    def addSet(self,other): # adds the other Set only if there is no overlap (returns True or False whether added or not)
        if self is not None and other is not None:
            if self.hasOverlap(other) == False:
                if other.cards:  # Check if the 'other' set is not empty
                    for card in other.cards:
                        self.addCard(card)
                    logging.debug("addSet(self,other): to existing set: " + self.printSet() + " added the set: " + other.printSet() )
                    return True
                else:
                    logging.warning("addSet(self, other): to existing set: " + self.printSet() + " could not add the set: " + other.printSet() + " 'other' set is empty!")
                logging.warning("addSet(self,other): to existing set: " + self.printSet() + " could not add the set: " + other.printSet() + " sets overlap!" )
                return False
        else:
            logging.warning("addSet(self,other): to existing set: " + self.printSet() + " could not add the set: " + other.printSet() + " One set is None!" )
            return False        

class SameValueCardSet(CardSet):
    def __init__(self, cards) -> None:
        self.dupe = "Veliko masno debelo!" # test for peculiar dissapearment of variables inherent to the child class
        super().__init__(cards)
        self.value = self.values[0] if self.values else None # self.values[0] # if self.values else None # self.value = cards[0].value
        self.numberOfCards = len(self.values) if self.values else None


    def printSet(self):
        printString = ""
        printString += self.dupe
        printString += "Same card set of cards with value: " + str(self.values[0]) # "Same card set of cards with value: " + str(self.values[0])+"\n" 
        printString += "Number of cards is : " + str(len(self.values)) + "\n" # printString += "Number of cards is : " + str(len(self.values)) + "\n"# "Number of cards is : " + str(self.numberOfCards) + "\n" # print("Number of cards is : ", self.numberOfCards)
        printString += super().printSet() 
        return printString

class Player:
    talon = CardSet([Card()])

    def __init__(self,name) -> None:
        self.name = name
        self.hand = None 
        self.points = 0 # points won by the player during the game, table + shtihovi (T-K+2c) are updated during the game 
        self.taken = 0 # total number of cards won/taken by the player in the end compares with player no2 and +3 points added to the one with larger number of cards taken 
        self.newPoints = 0
        self.newTaken = 0
        self.lastTakenInTurn = 0

 

    def printHand(self):
        print("Player: ", self.name, "\nCards in hand: ") #, end = "\t")
        print(self.hand.printSet()) 
        print("..........................................\n")

    def printStatus(self):
        print("\nplayer: ", self.name, "\nnew cards taken: ",self.newTaken,"\nnew points collected: ",self.newPoints,"\n", "\ntotal cards taken: ",self.taken,"\ntotal points: ",self.points,"\n..........................")
        

    def play(self,turnCount): 
        cardName = " "
        self.printHand()
        while cardName not in self.hand.names: 
            cardName = input("Pick a card to throw: ")
        cardPlayed = Card(cardName)
        self.hand.removeCard(cardPlayed)

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

    @classmethod
    def settleScore(cls, players: list):
        remainingCards = 0
        for name in Player.talon.names:
            remainingCards +=1
        if players[1].lastTakenInTurn >= players[0].lastTakenInTurn:
            players[1].points += Player.talon.totalPoints
            players[1].taken += remainingCards
        else:
            players[0].points += Player.talon.totalPoints
            players[0].taken += remainingCards
        if players[0].taken > players[1].taken:
            players[0].points += 3
        elif players[0].taken < players[1].taken:
            players[1].points += 3    
        if players[0].points > players[1].points :
            winner = players[0]
        elif players[1].points > players[0].points:
            winner = players[1]
        else:
            winner = None
        return winner
       

