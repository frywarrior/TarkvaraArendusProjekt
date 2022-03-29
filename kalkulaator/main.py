# Franco Kikkas ja Remo Sauks

from mata import *

print("Kalkulaator")
# Prindib pealkirja

c = mata()
# annab muutujale c klassi mata
a = float(input("Sisestage esimene arv: "))
# küsib kasutajalt esimest arvu

print("1 - liitmine, 2 - lahutamine, 3 - korrutamine, 4 - jagamine")
# prindib funktioonide listi
f = int(input("sisestage funktiooni number: "))
# küsib kasutajalt funktiooni nubrit
b = float(input("Sisestage teine arv: "))
# küsib kasutajalt teist arvu

if f == 1:
    # kui kasutaja valis esimese funktiooni, siis
    print(c.plus(a, b))
    # programm liidab ja prindib kahe küsitud arvu summa
elif f == 2:
    # kui kasutaja valis teise funktiooni, siis
    print(c.minus(a, b))
    # programm liidab ja prindib kahe küsitud arvu vahe
elif f == 3:
    # kui kasutaja valis kolmanda funktiooni, siis
    print(c.kor(a, b))
    # programm liidab ja prindib kahe küsitud arvu korrutise
elif f == 4:
    # kui kasutaja valis neljanda funktiooni, siis
    print(c.divi(a, b))
    # programm liidab ja prindib kahe küsitud arvu jagatise
else:
    # kui kasutaja sisestas funktiooni arvuks midagi muud, siis
    print("Sellist funktiooni pole")
    # programm prindib, et seda funktiooni ei ole