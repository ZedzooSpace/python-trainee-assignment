class MatrixError(Exception):
    """Базовое исключение библиотеки matrix_spiral."""


class MatrixNetworkError(MatrixError):
    """Ошибка при загрузке матрицы по сети или ошибка сервера."""


class MatrixFormatError(MatrixError):
    """Ошибка парсинга матрицы или нарушение условия квадратности."""