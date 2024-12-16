import pytest
from Klasowo import Point, Triangle, TriangleAnalyzer
import math

def test_contains_equilateral_triangle():
    """
    Testuje, czy znajduje trójkąt równoboczny bez punktów wewnątrz.
    """
    points = [Point(0, 0), Point(1, math.sqrt(3)), Point(2, 0), Point(1, 1)]
    analyzer = TriangleAnalyzer(points)
    assert analyzer.contains_equilateral_triangle() is True

def test_triangle_not_equilateral():
    """
    Testuje, że trójkąt nie jest równoboczny.
    """
    t = Triangle(Point(0, 0), Point(2, 0), Point(1, 1))
    assert not t.is_equilateral()

def test_triangle_area_zero():
    """
    Testuje, czy pole wynosi zero dla współliniowych punktów.
    """
    t = Triangle(Point(0, 0), Point(1, 1), Point(2, 2))
    assert t.area() == 0.0