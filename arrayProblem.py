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
                    



karte = [Card(x) for x in ["2s","Js","2c","As"]]
druge = [Card(y) for y in ["2h","Ts","2d","Ad"]]
pera = CardSet(karte)
mika = CardSet(druge)
pera.printSet()
print("a sad Mika...")
mika.printSet()
print("Setovi Pera i Mika se preklapaju: ", pera.hasOverlap(mika))
pera.addSet(mika)
pera.printSet()
print("a sad Mika...")
mika.printSet()
# print("pera i mika imaju iste karte: ",pera.__eq__(mika))
# zika = CardSet([Card("Dh"),Card("Td"),Card("As")])
# zika.printSet()
# zika.addCard(Card("Tc"))
# zika.printSet()
# # print(zika.switchCard(Card("Tc"),Card("3s")))
# zika.removeCard(Card("Td"))
# zika.printSet()