def list (n):
    ratio = 0
    result = [2]

    if n == 0:
        result = []

    for i in range(1, n):
        if i % 2 == 0:
            ratio -= 0.5
            result.append(result[0] + ratio)
        elif i % 2 == 1:
            result.append(-1)

    return result