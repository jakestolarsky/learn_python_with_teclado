class Pojazd:

    kolor = "bialy"

    def __init__(self, predkosc_max, milege):
        self.predkosc_max = predkosc_max
        self.milege = milege
        self.kolor = Pojazd.kolor

    def pokaz(self):
        _tuple = (self.predkosc_max, self.milege)
        return _tuple


class Bus(Pojazd):

    def __init__(self, nazwa, predkosc_max, milege):
        self.nazwa = nazwa
        super().__init__(predkosc_max, milege)
        self.kolor = Pojazd.kolor

    def pokaz(self):
        _tuple = (self.nazwa, self.predkosc_max, self.milege)
        return _tuple


class Samochod(Bus):

    def __init__(self, nazwa, predkosc_max, milege):
        super().__init__(nazwa, predkosc_max, milege)
        self.kolor = Pojazd.kolor



def main():
    pojazd = Pojazd(240, 18)
    print(pojazd.pokaz())

    bus = Bus("Shool Volvo", 180, 12)
    print(bus.pokaz())

    audi = Samochod("Audi Q5", 240, 18)
    print(audi.pokaz())

if __name__ == "__main__":
    main()