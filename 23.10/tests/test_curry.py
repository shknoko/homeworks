import sys
from pathlib import Path

import pytest

sys.path.append(f"{Path(__file__).parent.parent}")

from src.curry import curry


def test_curry_zero_args():
    def f():
        return range(10)

    curried = curry(f, 0)
    assert curried() == f()


def test_curry_one_arg():
    def f(a):
        return a

    curried = curry(f, 1)
    assert curried(2435234534252) == f(2435234534252)


def test_curry_two_args():
    def f(a, b):
        return a + b

    curried = curry(f, 2)
    assert curried(5)(10) == f(5, 10)


def test_curry_three_args():
    def f(a, b, c):
        return a - b & c

    curried = curry(f, 3)
    assert curried(2)(3)(4) == f(2, 3, 4)


def test_curry_insufficient_args():
    def add(a, b):
        return a + b

    curried = curry(add, 2)
    with pytest.raises(TypeError):
        curried(5)()
