import re

def sum_numbers_in_string(input_string: str) -> int:
    """
    Находит все целые числа в строке и возвращает их сумму.
    
    Args:
        input_string: Строка, в которой нужно найти числа.
        
    Returns:
        Сумма всех найденных целых чисел.
    """
    
    numbers = []
    current = ''
    for i in input_string:
        if i.isdigit():
            current += i
        else:
            if current:
                numbers.append(int(current))
                current = ''

    if current:
        numbers.append(int(current))
        
    return sum(numbers)

def sum_numbers_in_string_regex(input_string: str) -> int:
    """
    Находит все целые числа в строке и возвращает их сумму.
    
    Args:
        input_string: Строка, в которой нужно найти числа.
        
    Returns:
        Сумма всех найденных целых чисел.
    """
    

    nums = re.findall(r'\d+', input_string)

    return sum(int(i) for i in nums)