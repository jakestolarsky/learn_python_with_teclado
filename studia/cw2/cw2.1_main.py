import random

class Talia:

    def create():
        _karta_rodzaj = ["Kier", "Karo", "Trefl", "Pik"]
        _karta_wartosc = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

        _key_karty_kier =[]
        _key_karty_karo =[]
        _key_karty_trefl =[]
        _key_karty_pik =[]

        for i in _karta_wartosc:
            _key_karty_kier.append(_karta_rodzaj[0])
            _key_karty_karo.append(_karta_rodzaj[1])
            _key_karty_trefl.append(_karta_rodzaj[2])
            _key_karty_pik.append(_karta_rodzaj[3])

        _talia_kier = list(zip(_key_karty_kier, _karta_wartosc))
        _talia_karo = list(zip(_key_karty_karo, _karta_wartosc))
        _talia_trefl = list(zip(_key_karty_trefl, _karta_wartosc))
        _talia_pik = list(zip(_key_karty_pik, _karta_wartosc))

        _talia = []
        _talia.extend(_talia_kier)
        _talia.extend(_talia_karo)
        _talia.extend(_talia_trefl)
        _talia.extend(_talia_pik)
        return _talia

    def tasuj(talia):
        random.shuffle(talia)
        return talia

    def rozdaj(talia):
        _rand_numb = random.randrange(0, len(talia))
        _karta = talia[_rand_numb]
        talia.pop(_rand_numb)
        return print(_karta)

    def ilosc_kart(talia):
        return print(len(talia))

    def pokaz_karty(talia):
        return print(talia)


#create talia in variable
talia = Talia.create()
io_program = 1

while io_program == 1 :

    #menu
    user_input = input("\nMENU: \n 1. Liste kart \n 2. Ilosc kart \n 3. Potasowac karty \n 4. Wyciagnac z talii losowa karte \n 0. Zakoncz program \nTwoj wybor to: ")

    #user choose
    if (user_input == "0"):
        print("\n..koniec programu\n")
        io_program = 0
    elif (user_input == "1"):
        print("\nTwoja lista kart:")
        Talia.pokaz_karty(talia)
    elif (user_input == "2"):
        print ("\nTwoja liczba kart to: ")
        Talia.ilosc_kart(talia)
    elif (user_input == "3"):
        Talia.tasuj(talia)
        print("\n..karty potasowane")
    elif (user_input == "4"):
        print("\nTwoja losowa karta to: ")
        Talia.rozdaj(talia)
    else:
        print("\n..nie ma takiej komendy")