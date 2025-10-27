import sys
from pathlib import Path

import pytest

sys.path.append(f"{Path(__file__).parent.parent}")

from src.curry import curry, uncurry


def test_uncurry_zero_args():
    def f():
        return range(10)

    curried = curry(f, 0)
    uncurried = uncurry(curried)

    assert uncurried() == f()


def test_uncurry_one_arg():
    def f(a):
        return a

    curried = curry(f, 1)
    uncurried = uncurry(curried)

    assert uncurried(2435234534252) == f(2435234534252)


def test_uncurry_two_args():
    def f(a, b):
        return a + b

    curried = curry(f, 2)
    uncurried = uncurry(curried)

    assert uncurried(5, 10) == f(5, 10)


def test_uncurry_three_args():
    def f(a, b, c):
        return a - b & c

    curried = curry(f, 3)
    uncurried = uncurry(curried)

    assert uncurried(2, 3, 4) == f(2, 3, 4)


def test_uncurry_insufficient_args():
    def add(a, b):
        return a + b

    curried = curry(add, 2)
    uncurried = uncurry(curried)

    with pytest.raises(ValueError):
        uncurried(5)


def test_uncurry_excessive_args():
    def f(a, b):
        return a + b

    curried = curry(f, 2)
    uncurried_add = uncurry(curried)

    with pytest.raises(ValueError):
        uncurried_add(1, 2, 3)
