

print("Witaj w programie obliczającym NWW trzech liczb!")

a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
c = int(input("Podaj trzecia liczbe: "))

nww_1 = a *b
while b >0:
    r = a % b
    a = b
    b = r
nww_1 = nww_1 / a 

# Aby znaleść NWW dla kolejnej trzeciej liczby, szukamy NWW dla juz znalezionej przez nas liczby i trzeciej wprowadzonej przez użytkownika 
# d - NWW dla dwóch pierwszych liczb

nww_2 = c * nww_1
while nww_1 >0:
    r = c % nww_1
    c = nww_1
    nww_1 = r    
nww_2 = nww_2 / c 

# nww_2 - NWW dla znalezionej wczesniej liczby i trzeciej podanej przez użytkownika

print("NWW podanych liczb wynosi: ", nww_2)

