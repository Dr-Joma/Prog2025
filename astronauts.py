# GLOBÁLIS VÁLTOZÓK
# -------------------------------------

# 1 adatsor felépítése:
#   1. becenév
#   2. szerepkör: Pilóta, Mérnök, Kutató, Parancsnok, Orvos
#   3. teljesített küldetések száma
#   4. repült távolság (millió km)
#   5. aktuális célállomás

astronauts = [
    ["Nova-1", "Pilóta", 17, 1245.6, "Mars"],
    ["Echo-7", "Mérnök", 23, 2310.4, "Hold"],
    ["Lyra-3", "Kutató", 12, 845.2, "ISS"],
    ["Orion-X", "Parancsnok", 31, 3890.8, "Jupiter"],
    ["Zenith-5", "Orvos", 19, 1560.0, "Mars"],

    ["Vega-9", "Pilóta", 8, 430.5, "Hold"],
    ["Atlas-4", "Mérnök", 26, 2780.9, "Mars"],
    ["Cosmo-2", "Kutató", 14, 990.3, "ISS"],
    ["Helix-8", "Pilóta", 21, 1987.4, "Jupiter"],
    ["Pulse-6", "Orvos", 11, 620.0, "ISS"],

    ["Nebula-7", "Kutató", 29, 3105.1, "Saturnus"],
    ["Ion-3", "Mérnök", 16, 1340.7, "Hold"],
    ["Comet-1", "Pilóta", 34, 4120.9, "Mars"],
    ["Quasar-5", "Parancsnok", 41, 5022.6, "Neptunusz"],
    ["Orbit-8", "Orvos", 7, 390.2, "ISS"],

    ["Stellar-6", "Kutató", 18, 1625.8, "Vénusz"],
    ["Meteor-4", "Pilóta", 22, 2190.3, "Jupiter"],
    ["Lunar-9", "Mérnök", 5, 210.4, "Hold"],
    ["Void-2", "Kutató", 27, 2890.0, "Mars"],
    ["Solaris-7", "Parancsnok", 38, 4685.5, "Uranusz"],

    ["Cryo-5", "Orvos", 13, 910.6, "ISS"],
    ["Astro-1", "Pilóta", 3, 120.0, "Hold"],
    ["Zen-8", "Mérnök", 24, 2550.2, "Mars"],
    ["Photon-6", "Kutató", 9, 540.9, "Vénusz"],
    ["Draco-X", "Parancsnok", 45, 6200.0, "Plútó"]
]



# FELADATOK és FÜGGVÉNYEK
# -------------------------------------

# 1. feladat: Átlagosan hány küldetést teljesítettek eddig az űrhajósok?
#             Az eredményt kerekítés alkalmazása nélkül add meg!
''' KIÍRÁS MINTA
1. feladat:
    Az űrhajósok átlagosan 21 küldetést teljesítettek eddig.    
'''

def kuldetes_atlag():
    osszeg = 0
    for i in range(len(astronauts)):
        osszeg += astronauts[i][2]
    print(f"Urhajo atlag {(osszeg/len(astronauts)):.0f}")


# 2. feladat: Ha a célállomásáról senki sem indulna tovább addíg,
#             amíg mindenki célba nem ér,
#             akkor kik találkoznának az ISS űrállomáson?
#             A válaszban szerepkör szerinti csoportosításban
#             sorolja fel az űrhajósok neveit!
''' KIÍRÁS MINTA
2. feladat: ISS
    Kutató:
            Lyra-3
            Cosmo-2
    Orvos:
            Pulse-6
            Orbit-8
            Cryo-5
'''

def iss_talalkozo():
    szerepkorok = []
    for i in range(len(astronauts)):
        if astronauts[i][4] == "ISS" and astronauts[i][1] not in szerepkorok:
            szerepkorok.append(astronauts[i][1])
    
    for szerep in szerepkorok:
        print(f"\t{szerep}")
        for i in range(len(astronauts)):
            if astronauts[i][1] == szerep and astronauts[i][4] == "ISS":
                print(f"\t{astronauts[i][0]}")


# 3. feladat: Az összes repült távolság hány százaléka kötődik a pilótákhoz?
#             A százalék két tizedes pontossággal jelenjen meg.
''' KIÍRÁS MINTA
3. feladat: A pilóták által megtett távolság
    Össz. táv:     10094.7 millió km
    Arány:         19.20%
'''

def pilota_tav():
    pass


# 4. feladat: Az űrhajósok a küldetések száma alapján rangokat kapnak (csillagokat).
#             A Holdra utazó űrhajósok milyen rangúak?
#             Az adatokat táblázatos formában jelenítsd meg!
# Rang:
#    0  - 10 küldetés: *
#    11 - 20 küldetés: **
#    21 - 30 küldetés: ***
''' KIÍRÁS MINTA
4. feladat: A Holdra utazók rangjai

        Becenév     Rang
    ----------------------
    Echo-7           ***
    Vega-9            *
    Ion-3            **
    Lunar-9           *
    Astro-1           *
'''

def hold_rang():
    pass


# -------------------------------------
# PROGRAM
# -------------------------------------

print(f"\n{'*' * 70}\n*{'ŰRHAJÓSOK':^68}*\n{'*' * 70}\n")

kuldetes_atlag()
iss_talalkozo()
pilota_tav()
hold_rang()

print(f"\n{'BYE-BYE!':_>70}\n")




