import math

a = int(input("Podaj pierwsza liczbe z zakresu: "))

b = int(input("Podaj druga liczbe z zakresu: "))

if abs(a-b) > 20:
    s=(a+b)/2
    print("Podaje 6 najbliższych liczb najbliżej średniej (bez samej średniej),")
   
   #Wykorzystanie polecenia zaokrąglania w góre oraz w dół
    print(math.ceil(s-3))
    print(math.ceil(s-2))
    print(math.ceil(s-1))
    print(math.floor(s+1))
    print(math.floor(s+2))
    print(math.floor(s+3))

else:
    if a < b:
        while a <= b:
            print(a)
            a = a+1
            
    elif a==b:
        print("Podane liczby sa sobie równe.")

    else:
        while b <= a:
            print(b)
            b = b+1




