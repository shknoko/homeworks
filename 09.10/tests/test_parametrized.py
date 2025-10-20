import pytest
from conftest import random_list  # noqa: F401
from src.heap_sort import heap_sort


@pytest.mark.parametrize(
    ["arr", "expected"],
    [
        ([1, 5, 3, 2, 4], [1, 2, 3, 4, 5]),
        ([7, 6, 23423524], [6, 7, 23423524]),
        ([[], []]),
        ([5], [5]),
        ([2, 2, 2, 2], [2, 2, 2, 2]),
        ([0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]),
        ([12, -100, 47, -123, -5, 1, 0, -3], [-123, -100, -5, -3, 0, 1, 12, 47]),
    ],
)
def test_sort_parametrized(arr, expected):
    heap_sort(arr)
    assert arr == expected
