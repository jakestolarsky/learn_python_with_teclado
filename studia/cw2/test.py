
karta_rodzaj = ["Kier", "Karo", "Trefl", "Pik"]
karta_wartosc = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

talia_kier = {}


#ma wykonac ta petle tyle razy ile jest w karta_wartosc = 13
karty_kier = []

for i in karta_wartosc:
    karty_kier.append("Kier")

print(karty_kier)

talia_kier = {karty_kier[i]: karta_wartosc[i] for i in range(len(karta_wartosc))}

print(talia_kier)