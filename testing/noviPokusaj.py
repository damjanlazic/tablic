# ideja je da se ovo resi pomocu klase CardSubset jer ce tu biti mnogo lakse uporedjivati kombinacije

subsetCombinations = []

candidateIndex = 0
for combination in cardValueCombinations:
    cardCombination = []
    talonCopy = [card for card in talon]
    for value in combination:
        index = 0
        for card in talonCopy:
            if value == card.value and candidate.points <= card.points:
                candidate.copyCard(card)
                candidateIndex = index
            index += 1

        cardCombination.append(talonCopy[candidateIndex])
    combSubset = CardSubset(cardCombination)
    subsetCombinations.append(combSubset)
