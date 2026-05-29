def sort_segments(segments):
    """
    Сортирует отрезки по убыванию длины с использованием словаря,
    где ключи - длины, значения - списки отрезков
    
    Args:
        segments: список кортежей (start, end), представляющих отрезки
        
    Returns:
        список отрезков, отсортированных по убыванию длины
    """
    # TODO: Реализуйте функцию
    length_dict = {}
    for start, end in segments:
        length = end - start

        if length not in length_dict:
            length_dict[length] = []

        length_dict[length].append((start, end))

    result = []
    for length in sorted(length_dict.keys(), reverse=True):
        result.extend(length_dict[length])
    return result

# альтернативный простой вариант
def sort_segments_simple(segments):
    # TODO: Реализуйте простой вариант сортировки
    return sorted(segments, key=lambda x: x[1] - x[0], reverse=True)