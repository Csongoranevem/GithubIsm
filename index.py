print("Ezzel a programmal prímszámot számolhatsz és ellenőrizhetsz.\n")
szam=int(input("Írj be egy számot: "))



prim=False
if szam%2==0:
    print("Ez nem prim.")
if szam==2:
    print("Ez prim.")

for i in range(2,szam):
    if szam%i==0:
        break
    else:
        prim=True

if prim:
    print("Ez prim.")
else:
    print("Ez nem prim.")

