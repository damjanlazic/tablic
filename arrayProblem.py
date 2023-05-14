from karta import *

# class CardSet:
#     def __init__(self, cards) -> None:
#         self.cards = [card for card in cards]
#         self.names = [card.name for card in cards]
#         self.values = [card.value for card in cards]
#         self.points = [card.points for card in cards]
#         self.totalPoints = sum(self.points)
#     def printSet(self):
#         for n in self.names:
#             print(n,end = "\t")
#         print()
#         for v in self.values:
#             print(v,end = "\t")
#         print()
#         for p in self.points:
#             print(p,end = "\t")
#         print()
#         print("total points: ",self.totalPoints)
#     def __eq__(self, other):
#         if not hasattr(other, 'totalPoints'):
#             return False
#         if len(self.names) != len(other.names):
#              return False
#         for index in range(0,len(self.names)):
#                 if self.names[index] != other.names[index]:
#                      return False
#         return True
                    



# karte = [Card(x) for x in ["2s","Js","2c","As"]]
# druge = [Card(y) for y in ["2h","Ts","2d","Ad"]]
# pera = CardSet(karte)
# mika = CardSet(druge)
# pera.printSet()
# print("a sad Mika...")
# mika.printSet()
# print("Setovi Pera i Mika se preklapaju: ", pera.hasOverlap(mika))
# pera.addSet(mika)
# pera.printSet()
# print("a sad Mika...")
# mika.printSet()
# print("pera i mika imaju iste karte: ",pera.__eq__(mika))
# zika = CardSet([Card("Dh"),Card("Td"),Card("As")])
# zika.printSet()
# zika.addCard(Card("Tc"))
# zika.printSet()
# # print(zika.switchCard(Card("Tc"),Card("3s")))
# zika.removeCard(Card("Td"))
# zika.printSet()

talon = CardSet([Card(x) for x in ["2s","Js","2c","As","Tc","Ad","Td"]])

talonCopy = CardSet([Card("0")])
talonCopy.copySet(talon)
sameValueCards = []
print("set(talonCopy.values)",set(talonCopy.values))
for value in set(talonCopy.values):
        pendingCardSet = SameValueCardSet(talonCopy.findCardByValue(value))
        # pendingCardSet.printSet()

        if pendingCardSet.numberOfCards > 1:
            sameValueCards.append(pendingCardSet)

print("sameValueCards : ")
for setic in sameValueCards:
    setic.printSet()
print("......................")

combination = CardSet([Card(x) for x in ["2c","Tc","Ad"]])
cardCombinations = [combination]
# newCombination = CardSet([Card("0")])
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
                            if newCombination.__eq__(combination) == False:
                                # here need to check if the combination is already in cardCombinations 
                                if newCombination not in cardCombinations:
                                    cardCombinations.append(newCombination)
                                    addedCombination = True
# izmenja samo originalnu kombinaciju a ne i sve novonastale zato je dodat while addedCombinatino==true
print("kombinacije su:")
for combo in cardCombinations:
     combo.printSet()
# print("Posle brisanja clanova sa jednim elementom: ")
# for valueSet in sameValueCards:
#     valueSet.printSet()