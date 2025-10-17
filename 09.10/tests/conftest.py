import random

import pytest


@pytest.fixture
def random_list():
    list_len = random.randint(100, 5000)
    random_list = [random.randint(-10**11, 10**11) for _ in range(list_len)]
    return random_list
