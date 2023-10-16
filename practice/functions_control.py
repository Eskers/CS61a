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
    """Calculates the 3D Euclidian distance between two points
    (x1, y1, z1) and (x2, y2, z2).

    >>> distance3d(1, 1, 1, 1, 2, 1)
    1.0
    >>> distance3d(2, 3, 5, 5, 8, 3)
    6.164414002968976

    """
    x_diff = x2 - x1
    y_diff = y2 - y1
    z_diff = z2 - z1
    return sqrt(x_diff**2 + y_diff**2 + z_diff**2)


def harmonic(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic(2, 6)
    3.0
    >>> harmonic(1, 1)
    1.0
    >>> harmonic(2.5, 7.5)
    3.75

    """
    x_harmonic = 1 / x
    y_harmonic = 1 / y
    return 2 / (x_harmonic + y_harmonic)


def last_square(x):
    """Return the largest perfect square less than X, where X>0.

    >>> last_square(10)
    9
    >>> last_square(39)
    36
    >>> last_square(100)
    81
    >>> result = last_square(2) # Return, don't print
    >>> result
    1

    """
    i = 0
    while i**2 < x:
        i = i + 1
    return (i-1)**2


def overlaps(low0, high0, low1, high1):
    """Return whether the open intervals (LOW0, HIGH0) and (LOW1, HIGH1)
    overlap.

    >>> overlaps(10, 15, 14, 16)
    True
    >>> overlaps(10, 15, 1, 5)
    False
    >>> overlaps(10, 10, 9, 11)
    False
    >>> result = overlaps(1, 5, 0, 3)  # Return, don't print
    >>> result
    True

    """
    return
