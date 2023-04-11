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

    def copyCard(self, card):
        self.name = card.name
        self.value = card.value
        self.points = card.points

            
    def printCard(self):
        print(self.name, "\t", self.value, "\t", self.points )

class CardSubset:
    def __init__(self, cards) -> None:
        self.cards = [card for card in cards]
        self.names = [card.name for card in cards]
        self.values = [card.value for card in cards]
        self.points = [card.points for card in cards]
        self.totalPoints = sum(self.points)
    def printSubset(self):
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
# napraviti funkcije za dodavanje jednog subseta drugom i prepoznavanje da li je subset deo drugog subseta    
    def isCardInSubset(self,card): # checks if single card is in a subset (used in addCard() which is used in addSubset())
        for name in self.names:
            if name == card.name:
                return True
        return False
    
    def inSubset(self, other): # checks if other is a subset of the self
        for cardName in other.names:
            if cardName not in self.names:
                return False
        return True
    
    def hasOverlap(self,other): # checks if two subsets overlap and returns a subset with overlapping cards or returns False if no overlap
        if self.inSubset(other):
            return other
        elif other.inSubset(self):
            return self
        else:
            overlap = [] # I could use isCardInSubset() here but it seems pointless
            for name in other.names:
                if name in self.names:
                    overlap.append(Card(name))
            if overlap == []:
                return False
            else:
                return CardSubset(overlap)
    def addCard(self,card): # if card is already in subset returns False (no card added), otherwise it adds the card to subset and retruns True
        if self.isCardInSubset(card):
            return False # no card added
        self.cards.append(card)
        self.names.append(card.name)
        self.values.append(card.value)
        self.points.append(card.points)
        self.totalPoints += card.points
        return True # card added
    
    def addSubset(self,other): # adds the other subset only if there is no overlap (returns True of False whether added or not)
        if self.hasOverlap(other) == False:
            for card in other.cards:
                self.addCard(card)
            return True
        return False



class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.hand = [Card("Ah") for i in range(6)] # cards currently in hand / try to initialize it as empty list, than it is supposed to be a list of Card objects
        self.points = 0 # points won by the player during the game, table + shtihovi (T-K+2c) are updated during the game 
        self.taken = 0 # total number of cards won/taken by the player in the end compares with player no2 and +3 points added to the one with larger number of cards taken 
# this is necessary to be able to compare string names of different objects    
    def __eq__(self, other):
        if not hasattr(other, 'name'):
           return False
        return self.name == other.name

            
    def printHand(self):
        print("player: ", self.name, "\ncards in hand:")
        for i in self.hand:
            i.printCard()
    def printStatus(self):
        print("player: ", self.name, "\ncards taken: ",self.taken,"\npoints: ",self.points,"\n")

    # def findInTalon(valueCombination, talon):
    #     talonCopy = deepcopy(talon)
    #     cards = {} # idea is to have a dictionary where keys are cardValues and values are lists of cards on talon with those values
    #     for value in valueCombination:
    #         for card in talonCopy:
    #             if value == card.value:
    #                 cards[value].append(card)
        

    def play(self,talon):
        cardName = " "
        handNames = []
        for i in self.hand:
            handNames.append(i.name)
        
        while cardName not in handNames:
            cardName = input("Pick a card to throw: ")
        card = Card(cardName)
        maxIndex = len(self.hand)
        i = 0
        while i < maxIndex:
            if cardName.__eq__(self.hand[i].name):
                self.hand.pop(i)
                maxIndex -= 1
            i += 1

        # self.hand.remove(card)
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
                                cardValueCombinations.append(subset)
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
                                cardValueCombinations.append(subset)
                                print("ubacio subset: ",list(subset))        
            doAgain = False
            if card.value == 1 :
                card.value = 11
                doAgain = True
        i = 0
        cardCombinations = [list() for x in cardValueCombinations]
       
        for sub in cardValueCombinations:
            for val in sub:
                for c in talon:
                    if c.value == val:
                        doubles = False
                        for combinationIndex in range(len(cardCombinations)):
                            for ccardIndex in range(len(cardCombinations[combinationIndex])):
                                if c.value == cardCombinations[combinationIndex][ccardIndex].value:
                                    if c.points > cardCombinations[combinationIndex][ccardIndex].points:
                                        cardCombinations[combinationIndex][ccardIndex] = c        
                                        print("ccard=")
                                        cardCombinations[combinationIndex][ccardIndex].printCard()                        
                                    doubles = True
                            if not doubles: 
                                cardCombinations[combinationIndex].append(c)
                                print("combination.append(c)")
                                c.printCard()
        for combo in cardCombinations:
            print("combo:")
            for c1 in combo:
                print("c1:")
                c1.printCard()
            print("..........")

        takenAcard = False
        for cardSubset in cardCombinations:
            for cd in cardSubset:
                cd.printCard()
                takenAcard = True
                try:
                    talon.remove(cd)
                    self.points += cd.points
                    self.taken += 1
                #    print("evo me unutra!")
                except:
                #    print("naletosmo na duplikat")
                    pass
        print("\n")
        if takenAcard:
            self.points += card.points
            self.taken += 1
        else:
            talon.append(card)

        if len(talon) == 0:
            self.points += 1
                          

# talon = Card[] (talon ce da bude niz objekata klase Card)
# talonValues => for c in talon: talonValues.append(c.value) -> cilj dobiti niz integera koje mozemo koristiti u gore funkciji play 

