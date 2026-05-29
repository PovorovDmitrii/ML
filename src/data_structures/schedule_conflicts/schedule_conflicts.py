from datetime import datetime

def find_schedule_conflicts(intervals):
    """
    Находит все конфликтующие пары интервалов времени, включая интервалы через полночь.
    
    Аргументы:
        intervals: список кортежей вида [("HH:MM", "HH:MM"), ...]
        
    Возвращает:
        Список кортежей конфликтующих пар интервалов [(interval1, interval2), ...]
    """
    # TODO: Реализуйте функцию
    conflicts = []

    parsed_intervals = []

    for start, end in intervals:
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")

        parsed_intervals.append(((start, end), start_time, end_time))

    for i in range(len(parsed_intervals)):
        interval1, start1, end1 = parsed_intervals[i]
        for j in range(i + 1, len(parsed_intervals)):
            interval2, start2, end2 = parsed_intervals[j]

            # Проверяем пересечение интервалов
            if start1 < end2 and end1 > start2:
                conflicts.append((interval1, interval2))

    return conflicts