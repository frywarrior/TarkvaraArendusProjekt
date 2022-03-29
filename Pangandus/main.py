# Franco Kikkas IS21

from OOP_pangandus import *

import sys

fn = "data.txt"

print("Tere tulemast pythoni pangandusse! \n")

eesn = (str(input("Alustamiseks sisestage oma eesnimi: "))).capitalize()

peren = (str(input("\nJärgmiseks sisestage oma perekonnanimi: "))).capitalize()

x, aj = find(fn, eesn, peren)
if x == 1:
    print("Tundub et teil on juba kasutaja olemas!")
    kood = str(input("Sisselogimiseks palun sisestage oma kood: "))
    if kood == aj['pin']:
        print("Olete sisse logitud")
        age = aj['age']
        sugu = aj['gender']
        kood = aj['pin']
        bal = aj['balance']
        ne = 0
    else:
        print("kood on vale, proovige palun hiljem uuesti")
        sys.exit()
else:
    print("Tundub et teie nimelist kasutajat pole veel olemas...")
    kys = str(input("kas te soovite kasutjad luua? (ei või jah): "))
    if kys.lower() == "jah":
        age = str(input("Palun sisestage oma vanus: "))
        sugu = str(input("Nüüd palun sisestage oma sugu: "))
        kood = str(input("Nüüd lõpuks sisestage oma salajane kood: "))
        print(f"Teie kood: {kood}")
        bal = 0
        ne = 1
    else:
        print("Okei, head päeva")
        sys.exit()
p1 = Bank(eesn.capitalize(), peren.capitalize(), age, sugu, kood, bal)
p1.view_balance()

while True:
    print("Mida soovite järgmisena teha?")
    kys = int(input("1 - Raha sisestada, 2 Raha välja võtta, 3 - Konto detailid , 4 - Väljuda: "))
    if kys == 1:
        x = int(input("Kui palju soovite sisestada?: "))
        p1.deposit(x)
    elif kys == 2:
        x = int(input("Kui palju soovite välja võtta?: "))
        p1.withdraw(x)
    elif kys == 3:
        p1.view_balance()
    elif kys == 4:
        print("Head Päeva!")
        if ne == 1:
            new(fn, p1)
        else:
            replace(fn, p1)
        sys.exit()
    else:
        print("sellist võimalust me ei paku...")
