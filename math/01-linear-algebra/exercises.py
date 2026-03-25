from __future__ import annotations


def vector_add(left: list[float], right: list[float]) -> list[float]:
    if len(left) != len(right):
        raise ValueError("Vectors must have the same length")
    return [left_item + right_item for left_item, right_item in zip(left, right)]


def dot_product(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("Vectors must have the same length")
    return sum(left_item * right_item for left_item, right_item in zip(left, right))


def matrix_multiply(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    if not left or not right:
        raise ValueError("Matrices cannot be empty")

    left_column_count = len(left[0])
    right_row_count = len(right)

    if left_column_count != right_row_count:
        raise ValueError("Incompatible matrix dimensions")

    right_column_count = len(right[0])
    result: list[list[float]] = []

    for row in left:
        result_row: list[float] = []
        for column_index in range(right_column_count):
            column = [right[row_index][column_index] for row_index in range(right_row_count)]
            result_row.append(dot_product(row, column))
        result.append(result_row)

    return result


def run_examples() -> None:
    vector_a = [1, 2, 3]
    vector_b = [4, 5, 6]
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]

    print("Vector addition:", vector_add(vector_a, vector_b))
    print("Dot product:", dot_product(vector_a, vector_b))
    print("Matrix multiplication:", matrix_multiply(matrix_a, matrix_b))


if __name__ == "__main__":
    run_examples()