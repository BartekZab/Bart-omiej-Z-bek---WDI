from random import randint

los = randint(1,10)

odp = -1

i = 0 

print("Zgadnij liczbe z przedzialu od 1 do 10")
while odp != los:
    i += 1
    odp = int(input("POdaj liczbe: "))
    if odp > los:
        print("Niestety wylosowana liczba jest mniejsza od Twojej")
    elif  odp < los:
        print("Niestety wylosowana liczba jest wieksza od Twojej")
print("Brawo odgadles liczbe za", i, "razem")

