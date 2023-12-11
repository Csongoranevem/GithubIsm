print("Ezzel a programmal prímszámot számolhatsz és ellenőrizhetsz.\n")
szam=int(input("Írj be egy számot: "))



prim=False
if szam==1:
    print("Ez nem prim.")
elif szam==2:
    print("Ez prim.")
elif szam%2==0:
    print("Ez nem prim.")
else:
    for i in range(2,szam//2):
        if szam%i==0:
            break
    else:
        prim=True

    if prim:
        print("Ez prim.")
    else:
        print("Ez nem prim.")




