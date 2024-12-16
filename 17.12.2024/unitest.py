import unittest
from Klasowo import Point, Triangle, TriangleAnalyzer
import math

class TestTriangleAnalysis(unittest.TestCase):
    
    def test_is_equilateral(self):
        """
        Testuje czy trójkąt jest równoboczny.
        """
        t = Triangle(Point(0, 0), Point(1, math.sqrt(3)), Point(2, 0))
        self.assertTrue(t.is_equilateral())
        
    def test_area(self):
        """
        Testuje obliczanie pola trójkąta.
        """
        t = Triangle(Point(0, 0), Point(4, 0), Point(0, 3))
        self.assertAlmostEqual(t.area(), 6.0)
    
    def test_contains_point_exception(self):
        """
        Testuje czy rzucany jest wyjątek dla złego typu punktu.
        """
        t = Triangle(Point(0, 0), Point(1, 1), Point(0, 1))
        with self.assertRaises(AttributeError):
            t.contains_point((0, 0))  # Podano krotkę zamiast obiektu Point

if __name__ == "__main__":
    unittest.main()