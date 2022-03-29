class Isik:

    def __init__(self, eesnimi, perekonnanimi, kvalifikatsioon=1):
        self.ees = eesnimi
        self.pere = perekonnanimi
        self.kva = kvalifikatsioon

    def teave(self):
        print(f"Töötaja {self.ees} {self.pere}, kvalifikatsiooniga {self.kva}")

    def h2vita(self):
        print(f"Hüvasti, härra {self.ees} {self.pere}")
        del self
