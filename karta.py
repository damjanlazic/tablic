from itertools import combinations
from copy import deepcopy



class Card:
    def __init__(self, name) -> None:
        self.name = name
        try:
            self.value = int(self.name[0])
            if self.name == "2c":
                self.points = 1
            else:
                self.points = 0
        except:
            match self.name[0]:
                case 'T':
                    self.value = 10
                    if self.name[1] == "d" :
                        self.points = 2
                    else:
                        self.points = 1
                case 'J':
                    self.value = 12
                    self.points = 1
                case 'D':
                    self.value = 13
                    self.points = 1
                case 'K':
                    self.value = 14
                    self.points = 1
                case 'A':
                    self.value = 1
                    self.points = 1
    def __eq__(self, other):
        if not hasattr(other, 'name'):
           return False
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
    def __eq__(self, other):
        if not hasattr(other, 'totalPoints'):
            return False
        if len(self.names) != len(other.names):
             return False
        for index in range(0,len(self.names)):
                if self.names[index] != other.names[index]:
                     return False
        return True
# napraviti funkcije za dodavanje jednog Seta drugom i prepoznavanje da li je Set deo drugog Seta    
    def isCardInSet(self,card): # checks if single card is in a Set (used in addCard() which is used in addSet())
        for name in self.names:
            if name == card.name:
                return True
        return False
    
    def inSet(self, other): # checks if other is a sub-Set of the self
        for cardName in other.names:
            if cardName not in self.names:
                return False
        return True

# I probably only need to know do they overlap or not (True/False) but leave it like this for now...    
    def hasOverlap(self,other): # checks if two Sets overlap and returns a Set with overlapping cards or returns False if no overlap
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
        if self.isCardInSet(card) == False:
            print("Card you are trying to remove is not in the set!")
            card.printCard()
            return False # card you are trying to remove is not there
        index = 0
        for name in self.names:
            if name == card.name:
                self.names.pop(index)
                self.cards.pop(index)
                self.values.pop(index)
                self.points.pop(index)
                self.totalPoints -= card.points
                return True
            index += 1

    def findCardByValue(self, value):
    # since there could be more than one card with the same value in a set, we could get a list of cards, but 
    # for now it seems enough just to get the first one since we only need this method for replacing one card at a time
    #    cards = []
        for card in self.cards:
            if card.value == value:
                return card
    #            cards.append(card)
    #    return cards

    def switchCard(self,cardOut,cardIn):
        if self.isCardInSet(cardIn):
            print("No card added one of the two cards to be switched is already in set")
            return False # no card added
        index = 0
        for card in self.cards:
#            card.printCard()
            if card.__eq__(cardOut) == True:
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



class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.hand = CardSet([Card("0") for i in range(6)]) # cards currently in hand / try to initialize it as empty list, than it is supposed to be a list of Card objects
        self.points = 0 # points won by the player during the game, table + shtihovi (T-K+2c) are updated during the game 
        self.taken = 0 # total number of cards won/taken by the player in the end compares with player no2 and +3 points added to the one with larger number of cards taken 
        self.newPoints = 0
        self.newTaken = 0

# I don't need to compare two player objects?

    # def __eq__(self, other):
    #     if not hasattr(other, 'name'):
    #        return False
    #     return self.name == other.name

# obsolete: now use self.hand.printSet()    
    # def printHand(self):
    #     print("player: ", self.name, "\ncards in hand:")
    #     for i in self.hand:
    #         i.printCard()


    def printStatus(self):
        print("player: ", self.name, "\nnew cards taken: ",self.newTaken,"\nnew points collected: ",self.newPoints,"\n", "\ntotal cards taken: ",self.taken,"\ntotal points: ",self.points,"\n")

    # def findInTalon(valueCombination, talon):
    #     talonCopy = deepcopy(talon)
    #     cards = {} # idea is to have a dictionary where keys are cardValues and values are lists of cards on talon with those values
    #     for value in valueCombination:
    #         for card in talonCopy:
    #             if value == card.value:
    #                 cards[value].append(card)
        

    def play(self,talon):
        cardName = " "
        # handNames = []
        # for i in self.hand:
        #     handNames.append(i.name)
        
        while cardName not in self.hand.names: #handNames:
            cardName = input("Pick a card to throw: ")
        card = Card(cardName)
        self.hand.removeCard(card)

        # maxIndex = len(self.hand.names)
        # i = 0
        # while i < maxIndex:
        #     if cardName.__eq__(self.hand[i].name):
        #         self.hand.pop(i)
        #         maxIndex -= 1
        #     i += 1

        talonValues = []
        cardValueCombinations = []
        for c in talon:
            talonValues.append(c.value)
        doAgain = True
        while doAgain == True:
            for i in range(len(talonValues)+1):
                for subset in combinations(talonValues,i):
                    if sum(subset) == card.value:
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
                        if sum(subset) == card.value:
                            print("nasao subset: ",list(subset))
                            if subset not in cardValueCombinations: 
                                cardValueCombinations.append(list(subset))
                                print("ubacio subset: ",list(subset))        
            doAgain = False
            if card.value == 1 :
                card.value = 11
                doAgain = True
        
        for subset in cardValueCombinations:
            for i in range(len(subset)):
                if subset[i] == 11:
                    subset[i] = 1

        # cardCombinations = [list() for x in cardValueCombinations]
        cardCombinations = []
        
        candidate = Card("0")
        candidateIndex = 0
        listOfCandidateIndexes = []
        spare = Card("0")
        spareIndex = 0
        cardCombinationsIndex = 0
        for combination in cardValueCombinations:
            pendingCombination = []
            talonCopy = CardSet(talon)  # [Card(card.name) for card in talon]
            for value in combination:
                index = 0
                for card in talonCopy.cards:
                    # if value == card.value and candidate.points <= card.points:
                    if value == card.value:
                        if candidate.points <= card.points:
                            candidate.copyCard(card)
                            candidateIndex = index
                        else: 
                            spare.copyCard(card) # make a list of spare cards since you need them all
                            spareIndex = index     
                            # print("spare =",spareIndex)
                            spare.printCard()                 
                    index += 1

                pendingCombination.append(candidate)
                talonCopy.removeCard(candidate)
                candidate = Card("0")
            newCombination = CardSet(pendingCombination)
            pendingCombination = []
            replacedCard = True
            
            while replacedCard:
                combinationAlreadyExists = False
                replacedCard = False
                for combination in cardCombinations:
                    if combination.__eq__(newCombination):
                        combinationAlreadyExists = True
                        if spare.value in newCombination.values:
                            cardToReplace = newCombination.findCardByValue(spare.value)
                            if  newCombination.switchCard(cardToReplace,spare) == True: # the method swithCard replaces the card but returns true or false if the replacement
                                print("card replaced successfully")
                                replacedCard = True
                            else:
                                print("card we tried to replace is not there or the replacement is already there!")
            if combinationAlreadyExists == False:
                cardCombinations.append(newCombination)  
                                 
        print("Card combinations initial:")        
        for setOfCards in cardCombinations:
            setOfCards.printSet()
            print(".............")

        overlap = True
        getRidOf = []
        while overlap == True:
            overlap = False
            for index1 in range(len(cardCombinations)):
                for index2 in range(index1 + 1, len(cardCombinations)):
                    if cardCombinations[index1].hasOverlap(cardCombinations[index2]) == False:
                        cardCombinations[index1].addSet(cardCombinations[index2])
                        # getRidOf.append(index2)
                        overlap = True
# it's not neccessary to get rid of the added sets, and it causes index out of bounds this way so 
# I am getting rid of it alltoghether
            # for index in getRidOf:
            #     cardCombinations.pop(index)
            # getRidOf = []

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
            print("no card taken") # vidi sta ces s ovim
            takenAcard = False
        
        if takenAcard == True:
            # add the card that player played with
            self.points += card.points
            self.taken += 1

            print("Best set:")
            bestSet.printSet() 

            talonCopy = CardSet(talon)
            if len(talon) == len(bestSet.names): # +1 for tabla
                self.points += 1
                self.newPoints += 1
            for card in bestSet.cards:
                talonCopy.removeCard(card)
            self.points += bestSet.totalPoints
            self.taken += len(bestSet.names)
            
            self.newPoints = bestSet.totalPoints
            self.newTaken = len(bestSet.names)
      
            for card in talon:
                if talonCopy.isCardInSet(card) == False:
                    talon.remove(card)
        else:
            talon.append(card)
            self.newPoints = 0
            self.newTaken = 0

# ako ima dve karte iste vrednosti (npr. Ac i As) treba obe da budu u pojedinacnim kombinacijama
# ovo izgleda nije tako, nego vazi samo za karte koje imaju isti broj a razlicito poena nose
