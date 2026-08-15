def calculate_average(scores):
    if not scores:
        return 0

    return sum(scores) / len(scores)


scores = [80, 90, 100]

print(calculate_average(scores))