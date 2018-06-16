def sum_absolute(x):
    absolute = []

    for i in range(len(x)):
        absolute.append(abs(x[i]))

    return sum(absolute)
