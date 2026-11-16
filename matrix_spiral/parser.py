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
    for idx, row in enumerate(matrix, start=1):
        if len(row) != size:
            raise MatrixFormatError(
                f"Матрица не является квадратной: ожидалось {size} столбцов, "
                f"но в строке {idx} получено {len(row)}."
            )

    return matrix