import math
from itertools import combinations

class Point:
    """
    Klasa reprezentująca punkt na płaszczyźnie.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        """
        Oblicza odległość między dwoma punktami.
        """
        return math.dist((self.x, self.y), (other.x, other.y))

class Triangle:
    """
    Klasa reprezentująca trójkąt utworzony z trzech punktów.
    """
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def is_equilateral(self):
        """
        Sprawdza, czy trójkąt jest równoboczny.
        """
        d1 = self.p1.distance_to(self.p2)
        d2 = self.p2.distance_to(self.p3)
        d3 = self.p1.distance_to(self.p3)
        return math.isclose(d1, d2) and math.isclose(d2, d3)

    def area(self):
        """
        Oblicza pole trójkąta za pomocą wzoru Herona.
        """
        d1 = self.p1.distance_to(self.p2)
        d2 = self.p2.distance_to(self.p3)
        d3 = self.p1.distance_to(self.p3)
        s = (d1 + d2 + d3) / 2
        return math.sqrt(s * (s - d1) * (s - d2) * (s - d3))

    def contains_point(self, point):
        """
        Sprawdza, czy punkt znajduje się wewnątrz trójkąta.
        """
        t1 = Triangle(point, self.p2, self.p3)
        t2 = Triangle(self.p1, point, self.p3)
        t3 = Triangle(self.p1, self.p2, point)

        total_area = self.area()
        sub_areas = t1.area() + t2.area() + t3.area()

        return math.isclose(total_area, sub_areas)

class TriangleAnalyzer:
    """
    Klasa do analizy zbioru punktów pod kątem tworzenia trójkątów równobocznych.
    """
    def __init__(self, points):
        self.points = points

    def contains_equilateral_triangle(self):
        """
        Sprawdza, czy istnieje trójkąt równoboczny bez punktów wewnątrz.
        """
        for p1, p2, p3 in combinations(self.points, 3):
            triangle = Triangle(p1, p2, p3)
            if triangle.is_equilateral():
                if all(not triangle.contains_point(p) for p in self.points if p not in {p1, p2, p3}):
                    return True
        return False

# Przykład użycia

if __name__ == "__main__":
    # Równoboczny z punktem wewnątrz
    points1 = [
        Point(0, 0),
        Point(1, math.sqrt(3)),
        Point(2, 0),
        Point(1, 1)
    ]
    # Tworzy trójkąt równoboczny
    points2 = [
        Point(0, 0),
        Point(1, math.sqrt(3)),
        Point(2, 0),
    ]
 

    analyzer = TriangleAnalyzer(points1)
    result = analyzer.contains_equilateral_triangle()
    print(result)
