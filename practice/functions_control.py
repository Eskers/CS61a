from math import sqrt

def distance(x1, y1, x2, y2):
    """Calculates the Euclidian distance between two points (x1, y1)
    and (x2, y2)

    >>> distance(1, 1, 1, 2)
    1.0
    >>> distance(1, 3, 1, 1)
    2.0
    >>> distance(1, 2, 3, 4)
    2.8284271247461903
    """
    x_diff = x2 - x1
    y_diff = y2 - y1
    return sqrt(x_diff**2 + y_diff**2)


def distance3d(x1, y1, z1, x2, y2, z2):
    """Calculates the 3D Euclidian distance between two points (x1, y1, z1) and
    (x2, y2, z2).

    >>> distance3d(1, 1, 1, 1, 2, 1)
    1.0
    >>> distance3d(2, 3, 5, 5, 8, 3)
    6.164414002968976
    """
    x_diff = x2 - x1
    y_diff = y2 - y1
    z_diff = z2 - z1
    return sqrt(x_diff**2 + y_diff**2 + z_diff**2)
