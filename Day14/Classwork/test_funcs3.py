from funcs3 import matrix_max_elem, matrix_min_elem, matrix_sum
from matrix import Matrix


def test_max_element():
    matrix = Matrix(5, 5, 0, 9)
    assert matrix_max_elem(matrix) == max(max(matrix.data))


def test_min_elem():
    matrix = Matrix(5, 5, 0, 9)
    assert matrix_min_elem(matrix) == min(min(matrix.data))


def test_sum():
    matrix = Matrix(5, 5, 0, 9)
    sum = 0
    for i in matrix.data:
        for j in i:
            sum += j
    assert matrix_sum(matrix) == sum
