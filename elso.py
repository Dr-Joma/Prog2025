import random


szamok = []

# 100 elemu lista 1-99 kozott

for i in range (100):
    # szam generalas
    rszam = random.randint(1, 100)

    # szam elhelyezese a listaba
    szamok.append(rszam)
# ellenorzes
print(szamok)

# egyszamjatek
jatek_szam = 0
nem_talaltDB = 0

# kitalalando szam
kitalalando_szam = input()

