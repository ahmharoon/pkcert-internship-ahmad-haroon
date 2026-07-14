"""
Task 04 - Part A: NumPy Fundamentals (40 Marks)
1. 1D and multi-dimensional array creation methods
2. Indexing, slicing, reshaping, mathematical operations
3. Broadcasting
4. Vectorized operations vs loops
5. Linear algebra: dot product, matrix multiplication, transpose, inverse
"""

import time
import numpy as np


# ---------------------------------------------------------------------------
# 1. Array creation
# ---------------------------------------------------------------------------
def demonstrate_array_creation():
    print("=" * 60)
    print("1. Array Creation")
    print("=" * 60)

    from_list_1d = np.array([1, 2, 3, 4, 5])
    from_list_2d = np.array([[1, 2, 3], [4, 5, 6]])
    zeros = np.zeros((2, 3))
    ones = np.ones((3, 2))
    identity = np.eye(3)
    arange_arr = np.arange(0, 10, 2)
    linspace_arr = np.linspace(0, 1, 5)
    random_arr = np.random.default_rng(42).integers(0, 10, size=(2, 3))

    print("1D from list:\n", from_list_1d)
    print("2D from list:\n", from_list_2d)
    print("zeros(2,3):\n", zeros)
    print("ones(3,2):\n", ones)
    print("identity matrix (eye 3):\n", identity)
    print("arange(0,10,2):\n", arange_arr)
    print("linspace(0,1,5):\n", linspace_arr)
    print("random ints (2,3):\n", random_arr)
    print()


# ---------------------------------------------------------------------------
# 2. Indexing, slicing, reshaping, mathematical operations
# ---------------------------------------------------------------------------
def demonstrate_indexing_slicing_reshaping():
    print("=" * 60)
    print("2. Indexing, Slicing, Reshaping, Math Operations")
    print("=" * 60)

    arr = np.arange(1, 13)  # 1..12
    print("Original 1D array:", arr)

    print("Element at index 3:", arr[3])
    print("Slice [2:7]:", arr[2:7])
    print("Every 2nd element:", arr[::2])

    reshaped = arr.reshape(3, 4)
    print("Reshaped to (3,4):\n", reshaped)
    print("Row 1:", reshaped[1])
    print("Column 2:", reshaped[:, 2])
    print("Sub-matrix [0:2, 1:3]:\n", reshaped[0:2, 1:3])

    print("Sum:", reshaped.sum(), "| Mean:", reshaped.mean(), "| Max:", reshaped.max())
    print("Element-wise +10:\n", reshaped + 10)
    print("Element-wise square:\n", reshaped ** 2)
    print()


# ---------------------------------------------------------------------------
# 3. Broadcasting
# ---------------------------------------------------------------------------
def demonstrate_broadcasting():
    print("=" * 60)
    print("3. Broadcasting")
    print("=" * 60)

    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    row_vector = np.array([10, 20, 30])
    scalar = 100

    print("Matrix:\n", matrix)
    print("Matrix + row_vector (3,) broadcast across each row:\n", matrix + row_vector)
    print("Matrix + scalar (broadcast to every element):\n", matrix + scalar)

    column_vector = np.array([[1], [2], [3]])
    print("Matrix + column_vector (3,1) broadcast across each column:\n", matrix + column_vector)

    print(
        "\nAdvantage: broadcasting lets NumPy apply operations between arrays "
        "of different (but compatible) shapes without manually writing loops "
        "or duplicating data to match shapes, saving memory and being much "
        "faster than explicit Python-level looping."
    )
    print()


# ---------------------------------------------------------------------------
# 4. Vectorized operations vs loops
# ---------------------------------------------------------------------------
def demonstrate_vectorization_vs_loops():
    print("=" * 60)
    print("4. Vectorized Operations vs Traditional Loops")
    print("=" * 60)

    size = 2_000_000
    a = list(range(size))
    b = list(range(size))

    start = time.perf_counter()
    loop_result = [a[i] + b[i] for i in range(size)]
    loop_time = time.perf_counter() - start

    np_a = np.arange(size)
    np_b = np.arange(size)

    start = time.perf_counter()
    vector_result = np_a + np_b
    vector_time = time.perf_counter() - start

    print(f"Pure-Python loop time:  {loop_time:.5f} sec")
    print(f"NumPy vectorized time:  {vector_time:.5f} sec")
    print(f"Results match: {list(vector_result[:5])} == {loop_result[:5]}")
    print(f"Speedup: ~{loop_time / vector_time:.1f}x faster with vectorization")
    print()


# ---------------------------------------------------------------------------
# 5. Linear algebra
# ---------------------------------------------------------------------------
def demonstrate_linear_algebra():
    print("=" * 60)
    print("5. Linear Algebra")
    print("=" * 60)

    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    print("Dot product v1.v2:", np.dot(v1, v2))

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)
    print("Matrix multiplication A @ B:\n", A @ B)
    print("Transpose of A:\n", A.T)

    det = np.linalg.det(A)
    print("Determinant of A:", det)
    if det != 0:
        print("Inverse of A:\n", np.linalg.inv(A))
        print("Verify A @ inv(A) = Identity:\n", np.round(A @ np.linalg.inv(A)))
    else:
        print("A is singular - inverse does not exist.")
    print()


if __name__ == "__main__":
    demonstrate_array_creation()
    demonstrate_indexing_slicing_reshaping()
    demonstrate_broadcasting()
    demonstrate_vectorization_vs_loops()
    demonstrate_linear_algebra()
