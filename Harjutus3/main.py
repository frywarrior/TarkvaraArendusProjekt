from test_classes import *

isikud = [Isik("Franco", "Kikkas", 3), Isik("Torren", "Tamm", 4), Isik("Asmo", "Voitka")]

for isik in isikud:
    isik.teave()

last = min(isikud, key=lambda isik: isik.kva)

last.h2vita()
