import sys  # noqa: D100
sys.path.append('..')

from src.utils import create_shuffle_array, distance  # noqa: E402
from math import sqrt  # noqa: E402


def test_create_shuffle_array():  # noqa: D103
    # Setup
    n = 5
    array = create_shuffle_array(n)

    # Length
    assert len(array) == 5

    # Values
    val = True
    for i in range(n):
        if i not in array:
            val = False
            break
    assert val


def test_distance():
    # Setup
    a = (0, 0)
    b = (0, 3)
    c = (-7, 10)
    d = (23, -2)

    # Distance
    assert distance(a, b) == 3
    assert distance(c, d) == sqrt(1044)

    # Equivalence
    assert distance(c, d) == distance(d, c)
