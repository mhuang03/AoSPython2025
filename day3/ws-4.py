# Problem 4: Collinear Points
# Design a function that accepts a list of n tuples, each representing the coordinates
# of a point in 2D space, and returns True if all the points are collinear, and False otherwise.
# Two or more points are collinear if they all lie on the same straight line.
# Hint: Use the slope formula to calculate the slope of the line between points.

def slope(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 == x1:
        return None
    return (y2 - y1) / (x2 - x1)


def is_collinear(points):   # points is a list of pairs
    if len(points) <= 2:
        return True

    m = slope(points[0], points[1])
    for i in range(1, len(points) - 1):
        if slope(points[i], points[i+1]) != m:
            return False
    return True


print(is_collinear([(1, 1), (2, 2), (3, 3)]))
print(is_collinear([(1, 1), (2, 2), (3, 4)]))
print(is_collinear([(1, 1), (2, 1), (3, 1)]))
print(is_collinear([(1, 1), (1, 2), (1, 3)]))
