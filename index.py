print("Ezzel a programmal prímszámot számolhatsz és ellenőrizhetsz.\n")
szam=int(input("Írj be egy számot: "))



prim=True
if szam%2==0:
    prim=False
if szam==2:
    prim=True

for i in range(2,szam):
    if szam%i==0:
        prim=False
    else:
        prim=True

if prim==True:
    print("Ez prim.")
else:
    print("Ez nem prim.")

