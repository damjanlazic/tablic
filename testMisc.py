from karta import *

# def contains(cardName, listOfCards):
#     for card in listOfCards:
#         if cardName == card.name:
#             return True
#     return False
# def hasDuplicate(listOfLists,subList):
#     count = 0
#     subset2 = CardSet(subList)
#     for alist in listOfLists:
#         subset1 = CardSet(alist)
#         if subset1.__eq__(subset2):
#             count += 1
#     if count > 1:
#         return True
#     else:
#         return False

# cardCombinations = [[10,4],[10,4],[8,6]]
# cardCombinations = ((10,4),(10,4))
# setOfcardCombinations = set(cardCombinations)
# cardCombinations = ((Card("Ts"),Card("4s")),(Card("Tc"),Card("2s")))
# for cardSet in cardCombinations:
#     print("cardSet = ",cardSet)
#     for card in cardSet:
#         card.printCard()
# c = Card("As")
# for cardSet in cardCombinations:
#     # print("cardSet = ",cardSet)
#     for card in cardSet:
#         card = Card("As")
#         card.printCard()
#     # print("cardSet posle= ",cardSet)
# for cardSet in cardCombinations:
#     print("cardSet = ",cardSet)
#     for card in cardSet:
#         card.printCard()
# talon = [Card("Js"),Card("Td"),Card("As"),Card("2c"),Card("Ac")]

# if contains(cardCombinations, lambda x: x.value == c.value)  # True if any element has value = c.value

def calculateBestTake(cardCombinations,talonLength):
    combinationDict = {}
    maxPoints = 0
    for combo in cardCombinations:
        points = 0
        for card in combo:
            points += card.points
        if len(combo) == talonLength:
            points += 1
        if maxPoints < points:
            maxPoints = points
        combinationDict[points] = combo

    for points in combinationDict:
        print(points)
        for card in combinationDict[points]:
            card.printCard()
        print("...................")

    return combinationDict[maxPoints]

    # sortedCombinationDict = {}
    # for points in sorted(combinationDict):
    #     sortedCombinationDict[points] = combinationDict[points]

    # print("sortedCombinationDict")
    # for points in sortedCombinationDict:
    #     print(points)
    #     for card in sortedCombinationDict[points]:
    #         card.printCard()
    #     print("...................")
    
    # for points in sortedCombinationDict:
    #     i
    return sortedCombinationDict

class mockPlayer:
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
                        getRidOf.append(index2)
                        overlap = True
            for index in getRidOf:
                cardCombinations.pop(index)
            getRidOf = []

        print("Card combinations after recombination:")        
        for setOfCards in cardCombinations:
            setOfCards.printSet()
            print(".............")        

        if len(cardCombinations) > 0:
            bestSet = CardSet([card for card in cardCombinations[0].cards]) 
            for setOfCards in cardCombinations:
                if bestSet.totalPoints < setOfCards.totalPoints:
                    bestSet.copySet(setOfCards)
                elif bestSet.totalPoints == setOfCards.totalPoints:
                    if len(bestSet.names) < len(setOfCards.names):
                        bestSet.copySet(setOfCards)
        else:
            print("no card taken") # vidi sta ces s ovim
        
        print("Best set:")
        bestSet.printSet()        
        

#         # print("Calculate best take:")
#         # for c in calculateBestTake(cardCombinations,len(talon)):
#         #     c.printCard()        
#         print("---------------")

# # create a separate method which will try to combine combinations to get the max points gain,
# # then you can compare with below best combinations and decide which to use
# # now the problem is that it takes only one combination, and it could take more than one:
# # eg 7+6 =13 and 1 +2 =13 it should take both

#         pointsGain = 0
#         cardsTaken = 0
#         listOfbestCombinationsLists = []
#         pointsList = []
#         bestCombinationsDict = {}
#         while len(cardCombinations) > 0:
#             talonCopy = [card for card in talon]
#             for cardSet in cardCombinations:
#                 bestCombinationsList = []
#                 for cd in cardSet:
#                     if cd in talonCopy:
#                         cd.printCard()
#                         try:
#                             talonCopy.remove(cd)
#                             pointsGain += cd.points
#                             cardsTaken += 1
#                             bestCombinationsList.append(cd)
#                         #    print("evo me unutra!")
#                         except:
#                             print("evo nas u except bloku...")
#                             # ovde valjda treba da ponistim kombinaciju... ne, izgleda da to radim dole u else
#                     else:
#                         print("neku od ovih karata smo vec skinuli...", cd.printCard())
#                         pointsGain = 0
#                         cardsTaken = 0
#                         break
#                 if cardsTaken != 0:
#                     if len(talonCopy) == 0: # if all cards are taken in a combo one point is added for 'tabla'
#                         pointsGain += 1 
#                     pointsList.append(pointsGain)
#                     listOfbestCombinationsLists.append(bestCombinationsList)
#                 cardCombinations.remove(cardSet)
#                 pointsGain = 0
#                 cardsTaken = 0


#                 # for cardInList in bestCombinationsList:
#                 #     bestCombinationsDict[pointsGain].append(cardInList)
# #                bestCombinationsDict.update({pointsGain : bestCombinationsList}) 
#         print("...................///.................")
#         for a in listOfbestCombinationsLists:
#             for c in a:
#                 c.printCard()
#             print("...")
#         bestCombinationsDict = dict(zip(pointsList,listOfbestCombinationsLists))


#         for points in bestCombinationsDict:
#             print(points)
#             for card in bestCombinationsDict[points]:
#                 card.printCard()
#             print(".................../.................")
        
# # best pick:(highest number of points)        
#         for card in bestCombinationsDict[sorted(bestCombinationsDict)[len(bestCombinationsDict)-1]]:
#             card.printCard()
#         print("...................")        
# #        print(sorted(bestCombinationsDict)[len(bestCombinationsDict)-1])

#         # print("\n")
#         # if takenAcard:
#         #     self.points += card.points
#         #     self.taken += 1
#         # else:
#         #     talon.append(card)

#         # if len(talon) == 0:
#         #     self.points += 1


                    

                
                        
                        