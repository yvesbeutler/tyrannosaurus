from typing import List, Tuple, Callable
import math

# define some type alias
Vector = List[float]
Matrix = List[List[float]]

###################################
# Vector calculations
###################################

def add(v: Vector, w: Vector) -> Vector:
    """simple vector addition"""
    assert len(v) == len(w), 'Vectors need to have the same length'
    return [vi + wi for vi, wi in zip(v, w)]

def subtract(v: Vector, w: Vector) -> Vector:
    """simple vector subtraction"""
    assert len(v) == len(w), 'Vectors need to have the same length'
    return [vi - wi for vi, wi in zip(v, w)]

def scalar_multiply(c: float, v: Vector) -> Vector:
    """multiply a vector by a scalar"""
    return [c * vi for vi in v]

def vector_sum(vectors: List[Vector]) -> Vector:
    """sums all vector components together"""
    assert vectors, 'Vectors must not be empty'
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), 'Vectors need to have the same length'
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

def vector_mean(vectors: List[Vector]) -> Vector:
    """computes element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v: Vector, w: Vector) -> float:
    """
    computes the dot product (which is a scalar, not a vector)\n
    (v1 * w1) + (v2 * w2) + ... + (vn * wn)
    """
    assert len(v) == len(w), 'Vectors need to have the same length'
    return sum(vi * wi for vi, wi in zip(v, w))

def sum_of_squares(v: Vector) -> float:
    """computes the sum of squares for a single vector"""
    return dot(v, v)

def magnitude(v: Vector) -> float:
    """computes the magnitude (length) of a vector"""
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> float:
    """
    computes the square of the distance between two vectors\n
    (v1 - w1)^2 + (v2 - w2)^2  + ... + (vn - wn)^2
    """
    return sum_of_squares(subtract(v,w))

def distance(v: Vector, w: Vector) -> float:
    """computes the distance between two vectors"""
    return math.sqrt(squared_distance(v, w))

# run some checks
assert add([1,2,3],[4,5,6]) == [5,7,9]
assert subtract([5,7,9],[4,5,6]) == [1,2,3]
assert scalar_multiply(3, [2,4,8]) == [6,12,24]
assert vector_sum([[2,5,1], [2,6,3], [4,1,7]]) == [8,12,11]
assert vector_mean([[1,2], [3,4], [5,6]]) == [3,4]
assert dot([2,4,8], [3,1,4]) == 42
assert sum_of_squares([2,3,4]) == 29
assert magnitude([3,4]) == 5
assert squared_distance([1,4], [3,9]) == 29
assert distance([1,5], [5,8]) == 5

###################################
# Matrix calculations
###################################

def shape(A: Matrix) -> Tuple[int, int]:
    """returns the shape of a given matrix"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A: Matrix, i: int) -> Vector:
    """returns the i-th row"""
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    """returns the i-th column"""
    return [Ai[j] for Ai in A]

def gen_matrix(num_rows: int,
               num_cols: int,
               entry_fn: Callable[[int, int], float]) -> Matrix:
    """generates a matrix according to the specified number of
       rows and columns with its values generated by the entry function
    """
    return [[entry_fn(i, j)
            for j in range(num_cols)]
        for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
    """returns the n x n identity matrix"""
    return gen_matrix(n, n, lambda i, j: 1 if i == j else 0)

# run some checks
A: Matrix = [[1,2,3],[4,5,6]]
assert shape(A) == (2, 3)
assert get_row(A,1) == [4,5,6]
assert get_column(A,2) == [3,6]
assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]
