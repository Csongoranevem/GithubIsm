print("Ezzel a programmal prímszámot számolhatsz és ellenőrizhetsz.\n")
szam=int(input("Írj be egy számot: "))



def prim():
    if szam%2==0:
        return False
    if szam==2:
        return True

    
