while True:
    try:
        liczba=int(input("Wprowadz jakas liczbe: "))
        print(f"Wprowadzona przez Ciebie liczba to {liczba}")
        break
    except:
        print("Wprowadzona wartosc nie jest liczba")
