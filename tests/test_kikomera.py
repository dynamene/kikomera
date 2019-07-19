from index import Polygon, Point
import unittest

class TestPolygon(unittest.TestCase):
    def setUp(self):
        self.polygon = Polygon([Point(1, 2), Point(5, 6), Point(7, 1)])

    def test_Class(self):
        poly = self.polygon
        print(poly)

    def test_edges(self):
        new_class = Polygon([Point(1, 2), Point(5, 6), Point(7, 1)])
        assert type(new_class.edges) is list

    def test_contains(self):
        new_class = Polygon([Point(1, 2), Point(5, 6), Point(7, 1)])
        p1 = Point(3, 4)
        p2 = Point(5, 4)
        p3 = Point(1, 2)

        assert new_class.contains(p1) is True
        assert new_class.contains(p2) is False
        assert new_class.contains(p3) is True
