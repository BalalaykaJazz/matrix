import math
from itertools import chain


def create_matrix(name_matrix):

    size_new_matrix = input(f"Enter size of {name_matrix}matrix: ").split()
    print(f"Enter {name_matrix} matrix:")

    new_matrix = []
    for _ in range(0, int(size_new_matrix[0])):
        row = input().split()
        row_int = [int(float(x)) if int(float(x)) == float(x) else float(x) for x in row]
        new_matrix.append(row_int)

    return new_matrix


def get_matrix_param(matrix):

    size_rows = len(matrix)
    size_column = len(matrix[0]) if size_rows > 0 else 0

    return {"size_rows": int(size_rows), "size_column": int(size_column)}


def print_matrix(matrix):

    print("The result is:")

    size_max_element = len(str(max([x for k in matrix for x in k])))

    for row in matrix:

        whole_line = ""
        for cell in row:
            whole_line += str(cell).ljust(size_max_element + 1)

        print(whole_line)

    print("")


def round_matrix(matrix):

    result = [[round(y, 2) for y in x] for x in matrix]

    return result


# Addition in numeric matrix
def addition(matrix1, matrix2):

    result = [[m1 + m2 for m1, m2 in zip(row_matrix1, row_matrix2)]
              for row_matrix1, row_matrix2 in zip(matrix1, matrix2)]

    return result


def operation_add():

    first_matrix = create_matrix("first ")
    second_matrix = create_matrix("second ")

    size_matrix1 = get_matrix_param(first_matrix)
    size_matrix2 = get_matrix_param(second_matrix)

    if size_matrix1["size_rows"] != size_matrix2["size_rows"] \
            or size_matrix1["size_column"] != size_matrix2["size_column"]:
        print("The operation cannot be performed.")
    else:
        final_matrix = addition(first_matrix, second_matrix)
        final_matrix = round_matrix(final_matrix)
        print_matrix(final_matrix)


# Multiplication by number in numeric matrix
def multiplication_by_const(matrix, number):

    result = [[y * number for y in x] for x in matrix]

    return result


def operation_mult_by_const():

    matrix = create_matrix("")

    num_str = input("Enter constant: ")
    number = float(num_str) if '.' in num_str else int(num_str)

    final_matrix = multiplication_by_const(matrix, number)
    final_matrix = round_matrix(final_matrix)
    print_matrix(final_matrix)


# matrix by matrix multiplication in numeric matrix
def multiplication(matrix1, matrix2, size_matrix1, size_matrix2):

    _result = []
    for r_1 in range(0, size_matrix1["size_rows"]):

        matrix1_row = matrix1[r_1]
        new_row = []

        for c in range(0, size_matrix2["size_column"]):
            matrix2_cell = []
            for r_2 in range(0, size_matrix2["size_rows"]):
                matrix2_cell.append(matrix2[r_2][c])

            value = 0
            for i in range(0, size_matrix1["size_column"]):
                value += matrix1_row[i] * matrix2_cell[i]
            new_row.append(value)

        _result.append(new_row)

    return _result


def operation_mult():

    first_matrix = create_matrix("first ")
    second_matrix = create_matrix("second ")

    size_matrix1 = get_matrix_param(first_matrix)
    size_matrix2 = get_matrix_param(second_matrix)

    if size_matrix1["size_column"] != size_matrix2["size_rows"]:
        print("The operation cannot be performed.")
    else:
        final_matrix = multiplication(first_matrix, second_matrix, size_matrix1, size_matrix2)
        final_matrix = round_matrix(final_matrix)
        print_matrix(final_matrix)


# Transpose in numeric matrix
def transpose(matrix, size_matrix, _action):

    if _action == "4":  # Horizontal line
        matrix.reverse()
    elif _action == "3":  # Vertical line
        for i in matrix:
            i.reverse()
    elif _action == "2":  # Side diagonal

        final_matrix = []
        for r in range(0, size_matrix["size_rows"]):
            row = []
            for c in range(0, size_matrix["size_column"]):
                row.append(matrix[c][r])
            row.reverse()
            final_matrix.append(row)

        final_matrix.reverse()
        matrix = final_matrix

    elif _action == "1":  # Main diagonal

        final_matrix = []
        for r in range(0, size_matrix["size_rows"]):
            row = []
            for c in range(0, size_matrix["size_column"]):
                row.append(matrix[c][r])

            final_matrix.append(row)

        matrix = final_matrix

    return matrix


def operation_transpose(_action):

    matrix = create_matrix("")
    size_matrix = get_matrix_param(matrix)

    final_matrix = transpose(matrix, size_matrix, _action)
    print_matrix(final_matrix)


# Determined in numeric matrix
def calculate_determinant(matrix, size_matrix):

    if size_matrix == 1:

        result = matrix[0][0]

    elif size_matrix == 2:

        result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    else:

        result = 0
        for j in range(size_matrix):
            i = 0
            m2 = [[e for e in r] for r in matrix[1:]]
            for r in m2:
                r.pop(j)

            result += (matrix[i][j] * (-1) ** (1 + (j + 1)) * (calculate_determinant(m2, len(m2))))

    return result


def operation_determinant():

    matrix = create_matrix("")
    size_matrix = get_matrix_param(matrix)

    det = calculate_determinant(matrix, size_matrix["size_rows"])
    print("The result is:")
    print(det)


# Inverse matrix in numeric matrix
def calculate_cofactor(matrix, size_matrix, num_row):

    result = []
    for j in range(size_matrix):
        m2 = [[e for e in r] for r in matrix]
        for r in m2:
            r.pop(j)

        cofactor = pow(-1, num_row + 1 + j + 1) * (calculate_determinant(m2, len(m2)))
        result.append(cofactor)

    return _result


def inverse(matrix, size_matrix):

    det = calculate_determinant(matrix, size_matrix["size_rows"])

    if det == 0:
        print("This matrix doesn't have an inverse.")
        return []
    else:

        cofactor_matrix = []
        for j in range(size_matrix["size_rows"]):
            m = matrix.copy()
            m.pop(j)
            line = calculate_cofactor(m, size_matrix["size_rows"], j)
            cofactor_matrix.append(line)

        transpose_matrix = transpose(cofactor_matrix, size_matrix, "1")

        final_matrix = multiplication_by_const(transpose_matrix, 1 / det)

        rounded_matrix = [[int(x * 100) / 100 if x != 0 else 0 for x in i] for i in final_matrix]

        return rounded_matrix


def operation_inverse():

    matrix = create_matrix("")
    size_matrix = get_matrix_param(matrix)

    matrix = inverse(matrix, size_matrix)

    if matrix:
        print_matrix(matrix)


while True:
    print("1. Add matrices", "2. Multiply matrix by a constant", "3. Multiply matrices", "4. Transpose matrix",
          "5. Calculate a determinant", "6. Inverse matrix", "0. Exit", sep="\n")
    action = input("Your choice: ")

    if action == "0":
        break
    elif action == "1":
        operation_add()
    elif action == "2":
        operation_mult_by_const()
    elif action == "3":
        operation_mult()
    elif action == "4":
        print("1. Main diagonal", "2. Side diagonal", "3. Vertical line", "4. Horizontal line", sep="\n")
        action = input("Your choice: ")
        operation_transpose(action)
    elif action == "5":
        operation_determinant()
    elif action == "6":
        operation_inverse()