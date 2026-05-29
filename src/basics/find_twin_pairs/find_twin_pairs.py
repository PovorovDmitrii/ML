import math as m

def find_twin_pairs(X, threshold):
    """
    Находит все пары объектов, у которых евклидово расстояние меньше threshold.
    
    Аргументы:
    X -- двумерный список чисел (n x m)
    threshold -- пороговое значение расстояния
    
    Возвращает:
    Список кортежей (i, j, distance), где i < j и distance < threshold
    """
    result = []

    n = len(X)

    for i in range(n):
        for j in range(i + 1, n):
            dist = sum((a - b) ** 2 for a, b in zip(X[i], X[j])) ** 0.5

            if dist <= threshold:
                result.append((i, j, dist))

    return result

    