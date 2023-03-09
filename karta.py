from itertools import combinations



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
                case 'J':
                    self.value = 12
                case 'D':
                    self.value = 13
                case 'K':
                    self.value = 14
                case 'A':
                    self.value = 1
            self.points = 1
    def printCard(self):
        print(self.name, "\t", self.value, "\t", self.points )
   
class Player:
    def __init__(self,name,hand) -> None:
        self.name = name
        self.hand = hand # cards currently in hand
        self.points = 0 # points won by the player during the game, table + shtihovi (T-K+2c) are updated during the game 
        self.taken = 0 # total number of cards won/taken by the player in the end compares with player no2 and +3 points added to the one with larger number of cards taken 
        

    def play(self,talonValues):
        c = " "
        while c not in self.hand:
            c = input("Pick a card to throw: ")
        card = Card(c)
            
        for i in range(len(talonValues)+1):
            for subset in combinations(talonValues,i):
                if sum(subset) == card.value:
                    print(list(subset))
    # ako ima kec, odraditi ovo dva puta, jednom za value=1 a drugi put za value = 11 pa spojiti rezultate
        if 1 in talonValues:
            for i in range(len(talonValues)):
                if talonValues[i] == 1:
                    talonValues[i] = 11
                    break        
            for i in range(len(talonValues)+1):
                for subset in combinations(talonValues,i):
                    if sum(subset) == card.value:
                        print(list(subset))        


# talon = Card[] (talon ce da bude niz objekata klase Card)
# talonValues => for c in talon: talonValues.append(c.value) -> cilj dobiti niz integera koje mozemo koristiti u gore funkciji play 

