from random import shuffle
from math import sqrt


def create_shuffle_array(n):
    """Create a shuffle array of integer from 0 to n.

    Args:
        n (int): positive integer

    Returns:
        list: shuffle array
    """
    a = list(range(n))
    shuffle(a)
    return a


def distance(a, b):
    """Compute the 2D-distance between two point.

    Args:
        a (tuple): a point coordinates
        b (tuple): a point coordinates

    Returns:
        int: distance between a and b
    """
    xa, ya = a[0], a[1]
    xb, yb = b[0], b[1]
    return sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
