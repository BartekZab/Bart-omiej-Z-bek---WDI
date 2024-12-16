import math

def is_equilateral_triangle(p1, p2, p3):
    """
    Sprawdza, czy trzy punkty tworzą trójkąt równoboczny.
    """
    d1 = math.dist(p1, p2)
    d2 = math.dist(p2, p3)
    d3 = math.dist(p1, p3)
    return math.isclose(d1, d2) and math.isclose(d2, d3)

def is_point_inside_triangle(p, p1, p2, p3):
    """
    Sprawdza, czy punkt p znajduje się wewnątrz trójkąta utworzonego przez p1, p2, p3.
    """
    def area(p1, p2, p3):
        d1 = math.dist(p1, p2)
        d2 = math.dist(p2, p3)
        d3 = math.dist(p1, p3)
        s = (d1+d2+d3)/2  #Obliczanie połowy obwodu 
        area = math.sqrt(s * (s - d1) * (s - d2) * (s - d3))
        return area


    total_area = area(p1, p2, p3)
    area1 = area(p, p2, p3)
    area2 = area(p1, p, p3)
    area3 = area(p1, p2, p) 
    
    return math.isclose(total_area, area1 + area2 + area3)

def contains_equilateral_triangle(points):
    """
    Funkcja sprawdzająca, czy istnieje trójkąt równoboczny bez punktów wewnątrz.
    """
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                p1, p2, p3 = points[i], points[j], points[k]
                
                # Sprawdzamy, czy punkty tworzą trójkąt równoboczny
                if is_equilateral_triangle(p1, p2, p3):
                    # Sprawdzamy, czy nie ma żadnych innych punktów wewnątrz
                    if all(not is_point_inside_triangle(p, p1, p2, p3) for p in points if p not in {p1, p2, p3}):
                        return True
    return False
'''
dane = [(0,0),(1,3),(2,0),(1,math.sqrt(3)),(3,3),(5,1)]
print(contains_equilateral_triangle(dane))
'''

''' 
dane1 = [(0, 0), (1, 1), (2, 0)]  # Nie tworzy trójkąta równobocznego
dane2 = [(0, 0), (2, 0), (1, math.sqrt(3))]  # Tworzy trójkąt równoboczny
dane3 = [(0, 0), (2, 0), (1, math.sqrt(3)), (1, 1)]  # Równoboczny z punktem wewnątrz

print(contains_equilateral_triangle(dane1))  # False
print(contains_equilateral_triangle(dane2))  # True
print(contains_equilateral_triangle(dane3))  # False
'''