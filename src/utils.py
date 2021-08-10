from random import shuffle
import numpy as np


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


def change_position_array(a, b, positions):
    for i in range(len(positions) - 1):
        if i % 2 == 0:
            for j in range(positions[i], positions[i + 1]):
                pos = list(a).index(b[j])

                a[pos] = a[j]
                a[j] = b[j]

    return a


def distance(a, b):
    # xa, ya = a[0], a[1]
    # xb, yb = b[0], b[1]
    # return sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
    a = np.array(a)
    b = np.array(b)

    return np.linalg.norm(a - b)
