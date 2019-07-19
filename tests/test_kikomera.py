from index import Polygon, Point
import unittest

class TestPolygon(unittest.TestCase):
    def setUp(self):
        self.polygon = Polygon([Point(1, 2), Point(5, 6), Point(7, 1)])

    def test_Class(self):
        poly = self.polygon

    def test_edges(self):
        assert type(self.polygon.edges) is list

    def test_contains(self):
        p1 = Point(3, 4)
        p2 = Point(5, 4)
        p3 = Point(1, 2)

        assert self.polygon.contains(p1) is True
        assert self.polygon.contains(p2) is False
        assert self.polygon.contains(p3) is True
