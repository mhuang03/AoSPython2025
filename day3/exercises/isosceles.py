def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((y2 - y1)**2 + (x2 - x1)**2)**0.5


def is_isosceles(coords):  # coords = (p1, p2, p3) where p1 = (2,3), p2 = (4,5), etc.
    p1, p2, p3 = coords

    d1 = dist(p1, p2)
    d2 = dist(p2, p3)
    d3 = dist(p1, p3)

    distances = {d1, d2, d3}
    if len(distances) < 3:
        return True
    return False


print(is_isosceles(((1, 5), (5, 1), (7, 7))))
print(is_isosceles(((0, 0), (0, 3), (3, 0))))