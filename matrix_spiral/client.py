import httpx

from .exceptions import MatrixNetworkError
from .parser import parse_matrix
from .spiral_traversal import traverse_counter_clockwise

DEFAULT_TIMEOUT = 10.0


async def fetch_text(url: str, timeout: float = DEFAULT_TIMEOUT) -> str:
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.text
    except httpx.HTTPStatusError as exc:
        raise MatrixNetworkError(
            f"Сервер вернул ошибку HTTP {exc.response.status_code} при запросе к {url}"
        ) from exc
    except httpx.TimeoutException as exc:
        raise MatrixNetworkError(f"Превышено время ожидания ответа от {url}") from exc
    except httpx.RequestError as exc:
        raise MatrixNetworkError(f"Сетевая ошибка при обращении к {url}: {exc}") from exc


async def get_matrix(url: str) -> list[int]:

    raw_text = await fetch_text(url)
    matrix = parse_matrix(raw_text)
    return traverse_counter_clockwise(matrix)