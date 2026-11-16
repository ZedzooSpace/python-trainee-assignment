import asyncio
import unittest
from unittest.mock import AsyncMock, patch

import httpx

from matrix_spiral import MatrixNetworkError, get_matrix

SOURCE_URL = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]

SAMPLE_RESPONSE = """
+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
"""


def _mock_client(
    status_code: int = 200,
    text: str = "",
    side_effect: Exception | None = None,
) -> AsyncMock:
    client = AsyncMock()
    if side_effect:
        client.get.side_effect = side_effect
    else:
        request = httpx.Request("GET", SOURCE_URL)
        response = httpx.Response(status_code=status_code, text=text, request=request)
        client.get.return_value = response

    client_ctx = AsyncMock()
    client_ctx.__aenter__.return_value = client
    return client_ctx


class TestClient(unittest.IsolatedAsyncioTestCase):
    async def test_get_matrix_success(self) -> None:
        mock_ctx = _mock_client(status_code=200, text=SAMPLE_RESPONSE)
        with patch("httpx.AsyncClient", return_value=mock_ctx):
            result = await get_matrix(SOURCE_URL)
        self.assertEqual(result, TRAVERSAL)

    async def test_server_503_error(self) -> None:
        mock_ctx = _mock_client(status_code=503)
        with patch("httpx.AsyncClient", return_value=mock_ctx):
            with self.assertRaisesRegex(MatrixNetworkError, "HTTP 503"):
                await get_matrix("https://example.com/matrix.txt")

    async def test_connection_error(self) -> None:
        mock_ctx = _mock_client(side_effect=httpx.ConnectError("Connection refused"))
        with patch("httpx.AsyncClient", return_value=mock_ctx):
            with self.assertRaisesRegex(MatrixNetworkError, "Сетевая ошибка"):
                await get_matrix("https://example.com/matrix.txt")

    async def test_timeout_error(self) -> None:
        mock_ctx = _mock_client(side_effect=httpx.ReadTimeout("Timeout"))
        with patch("httpx.AsyncClient", return_value=mock_ctx):
            with self.assertRaisesRegex(MatrixNetworkError, "Превышено время ожидания"):
                await get_matrix("https://example.com/matrix.txt")

class TestAssignmentSync(unittest.TestCase):
    def test_assignment_sync_wrapper(self) -> None:
        mock_ctx = _mock_client(status_code=200, text=SAMPLE_RESPONSE)
        with patch("httpx.AsyncClient", return_value=mock_ctx):
            self.assertEqual(asyncio.run(get_matrix(SOURCE_URL)), TRAVERSAL)

if __name__ == "__main__":
    unittest.main()