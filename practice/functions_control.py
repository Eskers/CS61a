from math import sqrt

def distance(x1, y1, x2, y2):
    """Calculates the Euclidian distance between two points (x1, y1) and (x2, y2)

    >>> distance(1, 1, 1, 2)
    1.0
    >>> distance(1, 3, 1, 1)
    2.0
    >>> distance(1, 2, 3, 4)
    2.8284271247461903
    """
    x_diff = x2 - x1
    y_diff = y2 - y1
    return sqrt(x_diff ** 2 + y_diff ** 2)
