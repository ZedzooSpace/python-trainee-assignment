# matrix-spiral

Асинхронная Python-библиотека для загрузки квадратной матрицы ($N \times N$) по HTTP(S) и её обхода по спирали против часовой стрелки, начиная с левого верхнего угла.

## Быстрый старт и запуск тестов

1. **Установите зависимость (`httpx`):**
   ```bash
   pip install httpx
   ```

2. **Запустите все тесты:**
   ```bash
   python -m unittest discover -s tests -v
   ```

## Пример использования

```python
import asyncio
from matrix_spiral import get_matrix


async def main() -> None:
    url = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
    result = await get_matrix(url)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
```

## Структура проекта

* `matrix_spiral/` — исходный код библиотеки:
  * `client.py` — асинхронный HTTP-клиент (`get_matrix`) и обработка сетевых/HTTP ошибок (`MatrixNetworkError`).
  * `parser.py` — парсинг ASCII-таблицы и проверка квадратности матрицы (`MatrixFormatError`).
  * `spiral_traversal.py` — алгоритм обхода матрицы по спирали против часовой стрелки.
  * `exceptions.py` — пользовательские исключения библиотеки.
* `tests/` — юнит-тесты на стандартном `unittest` (алгоритм обхода, парсер, сетевые ошибки).