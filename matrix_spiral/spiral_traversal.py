def traverse_counter_clockwise(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []

    n = len(matrix)
    result: list[int] = []

    top, bottom = 0, n - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
        for row in range(top, bottom + 1):
            result.append(matrix[row][left])
        left += 1
        for col in range(left, right + 1):
            result.append(matrix[bottom][col])
        bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][right])
            right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[top][col])
            top += 1

    return result