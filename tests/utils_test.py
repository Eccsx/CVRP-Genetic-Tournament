import sys  # noqa: D100
sys.path.append('..')

from src.utils import create_shuffle_array  # noqa: E402


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
