# test_deck.py
from random import randrange
# from tablic import makeDeck, shuffle # mislim da mora da bude neka klasa
def makeDeck():
    deck=[]
    for suite in ("s","h","d","c"):
        for value in ("2","3","4","5","6","7","8","9","T","J","D","K","A"):
            deck.append(value + suite)
    return(deck)
def shuffle(cards) :
    cards=cards
    for i in range(0,len(cards)) :
        indexToSwitch=randrange(i,len(cards))
        cards[i], cards[indexToSwitch] = cards[indexToSwitch], cards[i]
    return cards

def test_makeDeck():
    deck = makeDeck()
    
    # Test if the deck has 52 cards
    assert len(deck) == 52
    
    # Test if the deck contains the right number of each suit (13 per suit)
    suits = ['s', 'h', 'd', 'c']
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "D", "K", "A"]
    
    for suit in suits:
        for value in values:
            assert value + suit in deck

def test_shuffle():
    deck = makeDeck()
    shuffled_deck = shuffle(deck[:])  # Use a copy of the deck to avoid mutating the original
    
    # Test that shuffled deck still contains 52 cards
    assert len(shuffled_deck) == 52
    
    # Test that all original cards are still in the shuffled deck
    original_deck = makeDeck()
    assert sorted(shuffled_deck) == sorted(original_deck)
    
    # Test that the order of the deck is likely changed (although this could occasionally fail by chance)
    assert shuffled_deck != original_deck
