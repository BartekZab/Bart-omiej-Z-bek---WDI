import time
import random
while True:
    
        print("Witaj w kalkulatorze Python! \nWprowadz dwie liczby a nastepnie znak dzialania ktore chcesz wykonać.\n(+) - dodawanie\n(-) - odejmowanie\n(*) - mnożenie\n(/) - dzielenie\n(#) - pierwiastkowanie\n(^) - potęgowanie\n(x) - losowanie z zakesu liczb\n(w) - wyjście")
        a=float(input("Pierwsza liczba: "))
        b=float(input("Druga liczba: "))
        dzialanie=input("Rodzaj wykonanego dzialania: ")
        
        if dzialanie == "+":
            print(f"Wynik to:\n{a} + {b} = {a+b}\n")
            time.sleep(2)
            

        elif dzialanie == "-":
            print(f"Wynik to:\n{a} - {b} = {a-b}\n")
            time.sleep(2)
        elif dzialanie == "*":
            print(f"Wynik to:\n{a} * {b} = {a*b}\n")
            time.sleep(2)
        elif dzialanie == "/":
            if b == 0:
                print("Nie wolno dzielic przez zero!\n")
                time.sleep(2)
            else:
                print(f"Wynik to:\n{a} / {b} = {a/b}\n")
                time.sleep(2)
        elif dzialanie == "#":
            if a < 0:
                print("Nie ma pierwiastka z liczby mniejszej od zera\n")
                time.sleep(2)
            else:
                print(f"Wynik to:\n{a} # {b} = {a**(1/b)}\n")
                time.sleep(2)
        elif dzialanie == "^":
            print(f"Wynik to:\n{a} ^ {b} = {a**b}\n")
            time.sleep(2)
        elif dzialanie == "x":
            print(f"Wylosowana liczba z zakresu {a} - {b} to: {random.randrange(int(a),int(b))}")
            time.sleep(2)
        elif dzialanie == "w":
            print("Dziekujemy za skorzystanie z naszego kalkulatora!")
            break
        else:
            print("Nie rozpoznano znaku.")
            time.sleep(2)

    #    if input("Czy chcesz wprowadzic nowe dane? (T / N)").strip().upper() != 'T':
    #         break
    #Cos nie dziala           
        
        





