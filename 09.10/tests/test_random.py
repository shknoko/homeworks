import pytest
from conftest import random_list  # noqa: F401
from src.heap_sort import heap_sort


@pytest.mark.repeat(100)
def test_sort_random(random_list):  # noqa: F811
    expected = sorted(random_list)
    heap_sort(random_list)

    assert random_list == expected
