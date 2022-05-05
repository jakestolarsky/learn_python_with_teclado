karta_rodzaj = ["Kier", "Karo", "Trefl", "Pik"]
karta_wartosc = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

key_karty_kier =[]
key_karty_karo =[]
key_karty_trefl =[]
key_karty_pik =[]

for i in karta_wartosc:
    key_karty_kier.append(karta_rodzaj[0])
    key_karty_karo.append(karta_rodzaj[1])
    key_karty_trefl.append(karta_rodzaj[2])
    key_karty_pik.append(karta_rodzaj[3])

talia_kier = list(zip(key_karty_kier, karta_wartosc))
talia_karo = list(zip(key_karty_karo, karta_wartosc))
talia_trefl = list(zip(key_karty_trefl, karta_wartosc))
talia_pik = list(zip(key_karty_pik, karta_wartosc))

talia = []
talia.extend(talia_kier)
talia.extend(talia_karo)
talia.extend(talia_trefl)
talia.extend(talia_pik)

print(talia)
print(len(talia))