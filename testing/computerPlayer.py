from karta import *

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.points = 0
        self.taken = 0
        self.newPoints = 0
        self.newTaken = 0
        self.lastTakenInTurn = 0

    def pickCard(self):
        theBestSet = CardSet(None) # None
        theBestCard = Card(None) # None
        for card in self.hand.cards:
            bestSet, takenAcard = self.evaluate_card(self.getCardCombinations(card))
            if bestSet is not None and bestSet.totalPoints > theBestSet.totalPoints:
                theBestSet = bestSet
                theBestCard = card  
                logging.debug("pickCard(self): if bestSet is not None and bestSet.totalPoints > theBestSet.totalPoints: %s \nThe best card: %s", [card.printCard() for card in theBestSet.cards], theBestCard.printCard())    
                
        if theBestSet.totalPoints == 0:
            for card in self.hand.cards:
                bestSet, takenAcard = self.evaluate_card(self.getCardCombinations(card))
                if bestSet is not None and len(bestSet.names) > len(theBestSet.names):
                    theBestSet = bestSet
                    theBestCard = card

        if theBestSet.totalPoints == -1:
            logging.debug("pickCard(self): theBestSet is CardSet(None) - No card can be taken!")
            theBestCard = self.hand.findMinValueCard()

        logging.debug("pickCard(self): theBestCard: %s", theBestCard.printCard())
        return theBestCard

        
    def play(self, turnCount): 

        cardPlayed = self.pickCard()
        self.hand.removeCard(cardPlayed)

        print("Computer played: " + cardPlayed.printCard())
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
