from .exceptions import MatrixFormatError


def parse_matrix(raw_text: str) -> list[list[int]]:
    matrix: list[list[int]] = []

    for line in raw_text.strip().splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("+"):
            continue

        if not (stripped.startswith("|") and stripped.endswith("|")):
            raise MatrixFormatError(f"Некорректный формат строки: {stripped!r}")

        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        try:
            row = [int(cell) for cell in cells]
        except ValueError as exc:
            raise MatrixFormatError("Ячейки матрицы должны содержать целые числа.") from exc

        if any(num < 0 for num in row):
            raise MatrixFormatError("Матрица должна содержать только неотрицательные числа.")

        matrix.append(row)

    if not matrix:
        raise MatrixFormatError("Получена пустая матрица.")

    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise MatrixFormatError(f"Матрица не является квадратной ({size}x{len(matrix[0])}).")

    return matrix