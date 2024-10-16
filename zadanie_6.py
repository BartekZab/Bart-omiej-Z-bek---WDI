a=int(input("Podaj pierwsza liczbe: "))
b=int(input("Podaj druga liczbe: "))

if a>=0 and b>0:
    print("Suma tych liczb to", a+b)
    print("Roznica tych liczb to", a-b)
    print("Iloczyn tych liczb to", a*b)
    print("Iloraz tych liczb to", a/b)
    print("Kwadrat pierwszej podanej liczby to", a**2)
    print("Kwadrat drugiej podanej liczby to", b**2)
    print("Pierwiastek pierwszej z podanych liczb to", round(a**(1/2),5))
    print("Pierwiastek drugiej z podanych liczb to", b**(1/2))

elif b==0:
    print("Nie dziel przez zero!")

elif a<0 and b>0:
    print("Suma tych liczb to", abs(a)+b)
    print("Roznica tych liczb to", abs(a)-b)
    print("Iloczyn tych liczb to", abs(a)*b)
    print("Iloraz tych liczb to", abs(a)/b)
    print("Kwadrat pierwszej podanej liczby to", abs(a)**2)
    print("Kwadrat drugiej podanej liczby to", b**2)
    print("Pierwiastek pierwszej z podanych liczb to", round(abs(a)**(1/2),5))
    print("Pierwiastek drugiej z podanych liczb to", b**(1/2))

elif b<0 and a>=0:
    print("Suma tych liczb to", a+abs(b))
    print("Roznica tych liczb to", a-abs(b))
    print("Iloczyn tych liczb to", a*abs(b))
    print("Iloraz tych liczb to", a/abs(b))
    print("Kwadrat pierwszej podanej liczby to", a**2)
    print("Kwadrat drugiej podanej liczby to", abs(b)**2)
    print("Pierwiastek pierwszej z podanych liczb to", round(a**(1/2),5))
    print("Pierwiastek drugiej z podanych liczb to", abs(b)**(1/2))
    

else:
    print("Podane przez ciebie liczby sa mniejsze od 0")


#Troche duzo tych printow ale ważne że działa ;)




   