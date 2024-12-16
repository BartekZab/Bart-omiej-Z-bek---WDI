def determinant(matrix):
    """
    Funkcja rekurencyjna do obliczania wyznacznika macierzy.
    Argumenty:
    matrix: lista list reprezentująca kwadratową macierz.

    Zwraca:
    Wyznacznik macierzy.
    """
    n = len(matrix)

    #Sprawdzanie czy macierz jest kwadratowa
    if not all(len(row) == n for row in matrix):
        return ValueError("Macierz musi być kwadratowa")

    #wyznacznik macierzy 1x1
    if n == 1:
        return matrix[0][0]

    #wyznacznik macierzy 2x2
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    #Rekurencyjne rozwinięcie Laplace'a
    det = 0
    for col in range(n):
        #Tworzenie macierzy dopełnień (minor)
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]

        # Oblicza współczynnik dopelnien
        cofactor = ((-1) ** col) * matrix[0][col]

        # Wyznacznik = suma iloczynów współczynników i wyznaczników minorów
        det += cofactor * determinant(minor)

    return det

# Przykłady użycia

macierz1 = [
    [2, -1, 3],
    [1,  0, 4],
    [5,  2, 0]
 ]
print(f"Wyznacznik macierzy 1: {determinant(macierz1)}")

macierz2 = [ 
    [1,5,3,8,1],
    [2,4,6,8,2],
    [2,5,4,3,5],
    [1,2,9,0,9],
    [1,3,2,5,6]
]

print(f"Wyznacznik macierzy 2: {determinant(macierz2)}")