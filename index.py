class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Polygon:
    def __init__(self, points):
        self.points = points

    @property
    def edges(self):
        ''' Returns a list of tuples that each contain 2 points of an edge '''
        edge_list = []
        for i, p in enumerate(self.points):
            p1 = p
            p2 = self.points[(i+1) % len(self.points)]
            edge_list.append((p1, p2))

        return edge_list

    def contains(self, P):
        _eps = 0.0000001

        inside = False

        for edge in self.edges:
            A, B = edge[0], edge[1]
            if A.y > B.y:
                A, B = B, A

            if P.y == A.y or P.y == B.y:
                P.y += _eps

            if P.x < min(A.x, B.x):
                inside = not inside
        return inside


if __name__ == "__main__":
    my_polygon = Polygon([Point(1, 2), Point(5, 6), Point(7, 1)])
    p1 = Point(5, 6)
    # p2 = Point(5, 4)
    # p3 = Point(4, 5)

    print("p1 in polygon: " + str(my_polygon.contains(p1)))
    # print("p2 in polygon: " + str(my_polygon.contains(p2)))
    # print("p3 in polygon: " + str(my_polygon.contains(p3)))
