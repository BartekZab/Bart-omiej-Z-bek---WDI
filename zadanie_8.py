wysokosc=int(input("Podaj wysokosc choinki: "))

a = "* " #Krok

#Stworzenie szpica w odpowiednim przesunieciu
print((wysokosc-1)*" ", "X") 


for i in range(2,wysokosc):
    print(" "*(wysokosc-i), a*i)
    i =-1

#Stworzenie pnia o odpowiednim przesunieciu podobnie jak szpic
print((wysokosc-1)*" ","U")