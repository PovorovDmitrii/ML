def find_anomalous_words(text: str ) -> list[str]:
    """
    Находит слова, длина которых отличается от средней длины слов в тексте более чем на 2 символа.

    :param text: Входная строка.
    :return: Список аномальных слов.
    """
    words = [w.strip(".,!?;:") for w in text.split()]
    words = [w for w in words if w]  
    


    if not words:
        return []
    
    avg_len = sum(len(word) for word in words) / len(words)

    result = []

    for word in words:
        if abs(len(word) - avg_len) >= 2:
            result.append(word)
    return result
    
