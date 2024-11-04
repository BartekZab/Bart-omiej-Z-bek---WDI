import random


#Wczytywanie danych od użytkownika:
n = int(input("Wprowadź ilosc losowych liczb do przedstawienia: "))
l = int(input("Wprowadź liczbe z dolnego zakresu: "))
m = int(input("Wprowadź liczbe z gornego zakresu: "))
if n < 0:
    raise ValueError("Długość listy nie może być ujemna.")
elif l > m:
    raise ValueError("Granica dolna musi być mniejsza lub równa granicy górnej.")

#Wypisanie listy
else:
    random_numbers = [random.randint(l, m) for _ in range(n) ]
    #print("Wygenerowane liczby: ", random_numbers )

def ciag(sequence):

    n = len(sequence)

    longest = []
    current = [sequence[0]]

    for i in range(1,n):
        if sequence[i] >= current [-1]:  # Sprawdzenie warunku ciągu słabo rosnącego
            current.append(sequence[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [sequence[i]] # Rozpoczynamy nowy podciąg

# Sprawdzamy ostatni podciąg, jeżeli jest dłuższy od ostatniego najdłuższego to zamieniamy go miejscem

    if len(current) > len(longest):
        longest = current 
    
    return longest

najdluzszy_ciag = ciag(random_numbers)
print("Najdłuższy rosnący podciąg:", najdluzszy_ciag)