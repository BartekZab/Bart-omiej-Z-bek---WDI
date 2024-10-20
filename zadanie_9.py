import time
saldo=5425
pin = 1234


while True:
    a=input("Witaj w swoim banku, aby uzyskac dostep do panelu użytkownika podaj PIN: ")
    try:
        if int(a)==pin:
            print(f"Poprawnie zalogowano na konto.\nJaki typ operacji chcesz wykonać?\n 1. Wpłata\n 2. Wypłata\n 3. Sprawdzenie salda\n 4. Wyjscie\n") 
            wybor=int(input(" "))
            if wybor==1:
                    wplata=int(input("Ile pieniędzy chcesz wpłacic? "))
                    saldo=saldo+wplata
                    print(f"Wpłacono {wplata} zlotych. Twoje aktualne saldo wynosi {saldo} zlotych\n")
                    time.sleep(2)
            elif wybor==2:
                    wyplata=int(input("Ile pieniedzy chcesz wyplacic ze swojego konta? "))
                    if wyplata > saldo:
                        print("Brak wystarczających srodkow na koncie.\n")
                        time.sleep(2) 
                    
                    else:
                        saldo=saldo-wyplata
                        print(f"Wyplacono {wyplata} zlotych. Twoje aktualne saldo to {saldo} zlotych\n")
                        time.sleep(2)

            elif wybor==3:
                    print("Twoje aktualne saldo to: ", saldo, "zlotych\n")
                    time.sleep(2)

            elif wybor==4:
                    print("Dziekujemy za skorzystanie z naszego banku. Do zobaczenia!")
                    break
            
            else:
                    print("Nie ma takiej opcji, wybierz ponownie.\n")
                    time.sleep(2)
        else:
                print("Podałeś zły PIN")
                break  
    except ValueError:
          print("Podales zly typ danych.")
          break


