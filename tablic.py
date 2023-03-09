# napravi spil karata i izmesaj ga
# prikazi spil pre i posle mesanja

from random import randrange
from karta import *

def napravispil():
    spil=[]
    for znak in ("s","h","d","c"):
        for vrednost in ("2","3","4","5","6","7","8","9","T","J","D","K","A"):
            spil.append(vrednost + znak)
    return(spil)
def mesaj(karte) :
    cards=karte
    
    for i in range(0,len(cards)) :
        indexzamene=randrange(i,len(cards))
    #    zamena=cards[indexzamene]
        cards[i], cards[indexzamene] = cards[indexzamene], cards[i]
    return cards

def deli(karte,brigraca):
    igrac = [["","","","","",""] for x in range(0,brigraca)]
# pravljeno za tablic tako da se dele po 3 karte za redom svakom igracu, br igraca moze biti 2 ili 4
    prva = 0
    poslednja = 3
    for deljenje in range(2):
        for i in range(0,brigraca):
            for k in range(prva,poslednja):
                igrac[i][k] = karte.pop(0)
                #
        prva = 3
        poslednja = 6           
    # player1 = Player(1,igrac[0])
    # player2 = Player(2,igrac[1])
    # players = [player1,player2]
    return igrac # players

def izbaciTalon(karte):
    talon = []
    for i in range(4):
        talon.append(karte.pop(len(karte)-1))
    return talon

# def baciKartu(talon):
#     print("Talon: ", talon)
#     karta = input("Izaberite kartu kojom igrate: ")
#     for x in range(len(talon)):
#         for y in range(1,len(talon)):
#             pass # ovde treba ona f-ja za pronalazenje combinacija imas u bookmarks


def main() :
    deck=napravispil()
    print(deck)
    izmesan=mesaj(deck)
    print(izmesan)
    print("broj karata je: ", len(izmesan))
    ruka=deli(izmesan,2)
    print(ruka)
    print("preostale karte\n", izmesan)
    print("broj preostalih karata je: ", len(izmesan))
    talon = izbaciTalon(izmesan)
    print("Na talonu su: \t", talon )
    print("preostale karte\n", izmesan)
    print("broj preostalih karata je: ", len(izmesan))

if __name__ == "__main__" :
    main()


