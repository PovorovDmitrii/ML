def pack_boxes(items, limit):
    """
    Упаковывает предметы в коробки, не превышая лимит веса.
    Предметы упаковываются в порядке следования.
    Предметы, превышающие лимит, исключаются из результата.
    
    Алгоритм:
    1. Фильтруем предметы, исключая те, что превышают лимит
    2. Инициализируем пустой список для коробок
    3. Для каждого предмета:
       - Если текущая коробка пуста или добавление предмета не превысит лимит,
         добавляем предмет в текущую коробку
       - Иначе, создаем новую коробку и добавляем туда предмет
    4. Возвращаем список коробок
    
    :param items: Список весов предметов
    :param limit: Максимальный вес коробки
    :return: Список коробок (список списков)
    """
    
    boxes = []
    current_box = []
    current_weight = 0

    for item in items:
        if item > limit:
            continue
        if current_weight + item <= limit:
            current_box.append(item)
            current_weight += item
        else:
            boxes.append(current_box)
            current_box = [item]
            current_weight = item
    if current_box:
        boxes.append(current_box)
    return boxes
    