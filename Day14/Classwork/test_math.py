from Math import Math


def test_sum():
    obj_math = Math(2, 2)
    assert 4 == obj_math.calc_sum()

def test_diff():
    obj_diff = Math(2, 2)
    assert 0 == obj_diff.calc_diff()

def test_mult():
    obj_mult = Math(2, 2)
    assert 4 == obj_mult.calc_mult()

def test_div():
    obj_div = Math(2, 2)
    assert 1 == obj_div.calc_div()
