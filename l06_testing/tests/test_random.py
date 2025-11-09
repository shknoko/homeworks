import pytest

from l06_testing.src.heap_sort import heap_sort


@pytest.mark.repeat(100)
def test_sort_random(random_list):  # noqa: F811
    expected = sorted(random_list)
    heap_sort(random_list)

    assert random_list == expected
