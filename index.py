print("Ezzel a programmal prímszámot számolhatsz és ellenőrizhetsz.\n")
szam=int(input("Írj be egy számot: "))



def prim():
    if szam%2==0:
        return False
    if szam==2:
        return True
    for i in range(szam):
        if szam%i==0:
            return False
            
    return True

if prim==True:
    print("Ez prim.")
else:
    print("Ez nem prim.")
    
