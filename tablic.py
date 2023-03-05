# napravi špil karata i izmešaj ga
# prikaži špil pre i posle mešanja

from random import randrange

def napravišpil():
    špil=[]
    for znak in ("s","h","d","c"):
        for vrednost in ("2","3","4","5","6","7","8","9","T","J","D","K","A"):
            špil.append(vrednost + znak)
    return(špil)
def mešaj(karte) :
    cards=karte
    
    for i in range(0,len(cards)) :
        indexzamene=randrange(i,len(cards))
    #    zamena=cards[indexzamene]
        cards[i], cards[indexzamene] =cards[indexzamene], cards[i]
    return cards

def deli(karte,brigrača):
    igrač = [["","","","","",""] for x in range(0,brigrača)]

# pravljeno za tablic tako da se dele po 3 karte za redom svakom igracu, br igraca moze biti 2 ili 4
    prva = 0
    poslednja = 3

    for deljenje in range(2):
        for i in range(0,brigrača):
            for k in range(prva,poslednja):
                igrač[i][k] = karte.pop(0)
                #
        prva = 3
        poslednja = 6           
    return igrač

def testfor():
    s="Udri me do zore!"
    list=["Bo","že","mi","li","ču","da","ve","li","ko","ga"]
    newlist=[]
    print(len(s))
#    for i in range(0,len(s)):
#       s[i]=
#        print("s[",i,"]=",s[i])

    print("a sad lista, 1. način for j in list...")
    for j in list:
        print(j)
       
#    print(list)
    print("2. način, for j in range(0,len(list))...")
    for j in range(0,len(list)):
        for i in range(j, len(s)):
            newlist.append(list[j]+s[i])
#            print(newlist[j])
    print("\nlista=", newlist)

def main() :
    deck=napravišpil()
    print(deck)
    izmešan=mešaj(deck)
    print(izmešan)
    print("broj karata je: ", len(izmešan))
    ruka=deli(izmešan,2)
    print(ruka)
    print("preostale karte\n", izmešan)
    print("broj preostalih karata je: ", len(izmešan))
main()


