def exponential():
    result = [x for x in range(1, 11)]

    for i in range(len(result)):
        result[i] = 2 ** result[i]

    return result