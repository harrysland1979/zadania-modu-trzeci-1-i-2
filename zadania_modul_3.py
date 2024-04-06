n = int(input("Podaj liczbę n: "))

print (n >= 100)

a = input("Napisz jaka jest Twoja ulubiona roślina: ")
if a == 'Skrzydłokwiat':
    print("Skrzydłokwiat jest najlepszą rośliną w historii!")
else:
    print("Nie, ja chcę Skrzydłokwiat...!")

dochod = float(input("Wprowadź swój roczny dochód: "))

if dochod < 85528:
    podatek = (dochod * 0.18) - 556.02
else:
    podatek = 14839.02 + ((dochod - 85528) * 0.32)

podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)


rok = int(input("Wprowadź rok: "))

if rok % 4 != 0:
    print("Zwykły zwykły")
elif rok % 100 != 0:
    print("Rok przestępny")
elif rok % 400 != 0:
    print("Zwykły rok")
else:
    print("Rok przestępny")


tajny_numer = int(input("Podaj liczbę całkowitą: "))
while tajny_numer != 777:
    print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")
    tajny_numer = int(input("Podaj liczbę całkowitą: "))
else:
    print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")


import time
for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")


slowo_kulucz = "pumpernikiel"
while True:
    slowo = input("Wprowadź słowo: ")
    if slowo == slowo_kulucz:
        print("Udało ci się opuścić pętlę.")
        break


slowo_uzytkownika = input("Wprowadź słowo: ")
slowo_uzytkownika = slowo_uzytkownika.upper()

for litera in slowo_uzytkownika:
    if litera == "A":
        continue
    elif litera == "E":
        continue
    elif litera == "I":
        continue
    elif litera == "O":
        continue
    elif litera == "U":
        continue
    else:
        print(litera)


slowo_bez_samoglosek = ""

slowo_uzytkownika = input("Wprowadź słowo: ")

slowo_uzytkownika = slowo_uzytkownika.upper()



for litera in slowo_uzytkownika:
    if litera == "A":
        continue
    elif litera == "E":
        continue
    elif litera == "I":
        continue
    elif litera == "O":
        continue
    elif litera == "U":
        continue
    else:
        slowo_bez_samoglosek += litera

print(slowo_bez_samoglosek)



blokow = int(input("Wprowadź liczbę bloków: "))

wysokosc = 0
bloki_w_warstwie = 1

while bloki_w_warstwie <= blokow:
    wysokosc += 1
    blokow -= bloki_w_warstwie
    bloki_w_warstwie += 1

print("Wysokość piramidy wynosi:", wysokosc)



liczba = int(input("Podaj liczbę całkowitą: "))
liczba_kroków = [liczba]
while liczba != 1:
    if liczba % 2 == 0:
        liczba = liczba / 2
    else:
        liczba = 3 * liczba + 1
    print(int(liczba))
    liczba_kroków.append(int(liczba))
print('Liczba kroków: ', len(liczba_kroków))
