import pytest
from func1 import *


def test_sum():
    a = 2
    b = 2
    assert calc_sum(a, b) == a + b


def test_diff():
    assert calc_diff(2, 2) == 2 - 2


def test_mult():
    assert calc_mult(2, 2) == 2 * 2


def test_div():
    assert calc_div(2, 2) == 2 / 2
