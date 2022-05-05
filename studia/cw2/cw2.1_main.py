"""
Zadanie 1
1. Napisz klasę Talia, która będzie zawierać inną klasę - klasę Karta, która spałnia następujące wymagania:
    - rodzaj (Kier, Karo, Trefl, Pik)
    - wartość (A,2,3,4,5,6,7,8,9,10,J,Q,K)
2. Dodaj metody:
    - rozdaj, aby pobrać pojedynczą kartę z talii - karta po rozdaniu usuwana jest z talii
    - przetasuj, która zapewnia że Talia składa się z 52 kart i ustawia je w sposób losowy
"""

class Talia:
    
    #inicjalizuj talie ze wszystkimi kartami
    def __init__(self):
        self.kart = self.Karta()

    #pobieraj pojedyncza karte z talii po czym jest usowana z talii
    def rozdaj():
        pass

    #tasuje wszystkie 52 karty i ustawia je w sposob losowy
    def przetasuj():
        pass

    #inner class Karta
    class Karta:
        
        def __init__(self):
            self.rodzaj = ["Kier", "Karo", "Trefl", "Pik"]
            self.wartosc = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        
        def display(self):
            print("Rodzaj: ", self.rodzaj)
            print("Wartosc: ", self.wartosc)


Talia.kart.display()
