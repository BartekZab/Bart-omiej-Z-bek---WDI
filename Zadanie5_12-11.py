
try:    
    n = int(input("Podaj wymiar tablicy (n): "))
except:
    print("WPROWADZONO NIE POPRAWNY TYP DANYCH")
    exit()
if n > 0:   
   
    def fibo(n):
        "Funkcja deneruje ciag Fibonacciego"
        fib_sequence = []
        a, b = 0, 1
        for _ in range(n):
            fib_sequence.append(a)
            a, b = b, a+b
        return fib_sequence

    def fill_spiral(matrix):
        "Funkcja wypelniajaca macierz w kolejnosci spiralnej"
        n = len(matrix)
        top, bottom, left, right = 0, n - 1, 0, n - 1
        index = 0
        fib_sequence = fibo(n * n)
        
        while top <= bottom and left <= right:
            #Petla wypelniajaca gorny rząd
            for i in range(left, right + 1):
                matrix[top][i] = fib_sequence[index]
                index += 1
            top += 1
            # Wypełnianie prawej kolumny
            for i in range(top, bottom + 1):
                matrix[i][right] = fib_sequence[index]
                index += 1
            right -= 1

            if top <= bottom:
                # Wypełnianie dolnego rzędu
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = fib_sequence[index]
                    index += 1
                bottom -= 1

            if left <= right:
                # Wypełnianie lewej kolumny
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = fib_sequence[index]
                    index += 1
                left += 1

    
        
<<<<<<< HEAD
matrix = [[0] * n for _ in range(n)]  # Tworzenie dwuwymiarowej tablicy nxn
fill_spiral(matrix)
=======
        matrix = [[0] * n for _ in range(n)]  # Tworzenie dwuwymiarowej tablicy nxn
        fill_spiral(matrix)
        
        # Wyświetlanie tablicy
        for row in matrix:
            print(" ".join([str(x) for x in row]))
>>>>>>> 34fdd18c9aca0963e2eab3ee76722e574aee12c3

# Wyświetlanie tablicy
for row in matrix:
    print(" ".join(map(str, row)))

    

else:
    print("Wymiary tablicy musza byc wieksze od zera")
    
#Przykladowe wyniki

'''
n = 5

0 1 1 2 3
610 987 1597 2584 5
377 28657 46368 4181 8
233 17711 10946 6765 13
144 89 55 34 21


n = 8

0 1 1 2 3 5 8 13
196418 317811 514229 832040 1346269 2178309 3524578 21
121393 2971215073 4807526976 7778742049 12586269025 20365011074 5702887 34
75025 1836311903 956722026041 1548008755920 2504730781961 32951280099 9227465 55
46368 1134903170 591286729879 6557470319842 4052739537881 53316291173 14930352 89
28657 701408733 365435296162 225851433717 139583862445 86267571272 24157817 144
17711 433494437 267914296 165580141 102334155 63245986 39088169 233
10946 6765 4181 2584 1597 987 610 377

'''

