n = int(input("Podaj wymiar tablicy (n): "))
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

    
        
matrix = [[0] * n for _ in range(n)]  # Tworzenie dwuwymiarowej tablicy nxn
fill_spiral(matrix)

# Wyświetlanie tablicy
for row in matrix:
    print(" ".join(map(str, row)))

    

else:
    print("Wymiary tablicy musza byc wieksze od zera")
    