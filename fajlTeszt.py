# Fajlbeolvasas eljarassal

verseny_adatok = []
inputfajl = "F1-2024dec.csv"

def adat_beolvasasa(fajlnev):
    try:
        with open (fajlnev,encoding="utf-8") as fajl:
            global verseny_adatok
            verseny_adatok = fajl.readlines()
        
    except Exception as ex:
        print(f"ezer van baj mo: {ex}")
    except FileNotFoundError:
        print("hiva a fajl nyitas kozbe")

# Eljaras
def pontatlanok():
    # 1. Hany versenyzo nem szerzett meg pontot?
    db = 0
    for i in range (1, len(verseny_adatok)):
        if (int(verseny_adatok[i].split(',')[1]) == 0):
            db = db + 1
    print("Nem kaptak pontot szama:",db)    

# Fuggveny
def kereso(nev):
    # 2. Van-e Fernando nevu versenyzo?
    i = 0
    while (i<len(verseny_adatok) and nev not in verseny_adatok[i]):
        i = i + 1
    if (i<len(verseny_adatok)):
        return True
    else:
        return False

# Eljaras
def csapat(nev):
    i = 1
    while i<len(verseny_adatok) and "Pierre Gasly" not in verseny_adatok[i]:
        i = i + 1
        
    if i<len(verseny_adatok):
        print(nev,verseny_adatok[i].split(',')[2].strip(),"csapatban van")
    else:
        print("Pierre Gasly nINCS")

# Fuggveny
def csapattagok(csapatnev):
    dih = 0
    masik = []
    
    for i in range(2,len(verseny_adatok)):
        if verseny_adatok[i].split(',')[2].strip()==csapatnev:
            dih=dih+1
            masik.append(verseny_adatok[i].split(',')[0])
    return masik

# Megint 2. Mindenki szerzett 90 pontot?
def fasz(fasz2):
    i = 0
    while (i<len(verseny_adatok) and int(verseny_adatok[i].split(',')[1] ))>90:
        i = i + 1
    if i==len(verseny_adatok):
        print("ye yeah")
    else:
        print("o heil nah")

""" 
'''
    1.  [] Megszámolás
    2.  [] Eldöntés 1, 2
    3.  [] Kiválasztás
    4.  [] Keresés
    5.  [] Sorozatszámítás // Összegzés
    6.  [] Minimum // Maximum kiválasztás
    7.  [] Másolás
    8.  [] Kiválogatás
    9.  [] Szétválogatás
    10. [] Metszet
    11. [] Unió
    
    12. [] Rendezés
        [] Egyszerű cserés
        [] Buborékos
        [] Minimum kiválasztásos
'''

#-------------------------------






# 3. Melyik istallo pilotaja a yuki tsunoda?

while (verseny_adatok[i].split(',')[0]!="Yuki Tsunoda"):
    i = i + 1
print("Yuki Tsunoda a",verseny_adatok[i].split(',')[2],"istalo tadgja")

# 5. Szamold ki a versenyzok pontszamainak atlagat

S = 0
for i in range(len(verseny_adatok)):
    S += int(verseny_adatok[i].split(',')[1])
print(f"Versenyzok pontszamainak atlaga:",{S/len(verseny_adatok)-1})

# 6. Ki szerezte a legtobb pontot? pontok lacikam pontok

maxi = 1
max = verseny_adatok[i].split(',')[1]
for i in range(2,len(verseny_adatok)):
    if verseny_adatok[i]>verseny_adatok[maxi]:
        maxi=i
        max=verseny_adatok[i]

# 7. Kinek van a legkevesebb pontja? pontok lacikam pontok

mini = 1
min = verseny_adatok[i].split(',')[1]
for i in range(2,len(verseny_adatok)):
    if verseny_adatok[i]<verseny_adatok[mini]:
        mini=i
        min=verseny_adatok[i]
print("A legkeveseb pontal rendelkzp nber:",verseny_adatok[mini].split(',')[0])

# 9. Kinek van pontja meg kinek nincs?

dby=0
dbz=0
y=[]
z=[]
for i in range(1, len(verseny_adatok)):
    if (int(verseny_adatok[i].split(',')[1]>0)):
        dby+=1
        y.append(verseny_adatok[i].split(',')[0])
    else:
        dbz+=1
        z.append(verseny_adatok[i].split(',')[0])
print(f"Van pontypetya:{y}")
print(f"Nincs pontypetya:{z}")

# 10. Versenyzok pontszama alapjan novekvo

for i in range(1,len(verseny_adatok)-1):
    min=i
    minertek=int(verseny_adatok[i].split(',')[1])
    for j in range(i+1,len(verseny_adatok)):
        if(int(verseny_adatok[j].split(',')[1]) < int(verseny_adatok[min].split(',')[1])):
            min=j
            minertek=int(verseny_adatok[j].split(',')[1])
    s=verseny_adatok[i]
    verseny_adatok[i]=verseny_adatok[min]
    verseny_adatok[min]=s """
    
adat_beolvasasa(inputfajl)

pontatlanok()

van_e = kereso("Fernando")
if van_e:
    print("Van Fernando")
else:
    print("Nincs Fernando")

csapat("Pierre Gasly")

csapatnev = "mcaklren"
tag_lista = csapattagok(csapatnev)
print(f"{csapatnev} tagjai:")
i=1
for nev in tag_lista:
    print(f"{i},{nev:>30}")
    i+=1



print("END")





