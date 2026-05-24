from typing import Callable, List

def filter_strings(condition: Callable[[str], bool], strings: List[str]) -> List[str]:
    """
    Принимает лямбда-функцию (condition) и список строк (strings).
    Возвращает новый список, в котором остались только те строки, 
    для которых лямбда-функция вернула True.
    """
    # Встроенная функция filter применяет наше условие ко всем элементам
    return list(filter(condition, strings))

if __name__ == "__main__":
    # Тестовый массив строк
    test_words = ["hello", "world", "a cat", "apple", "sun", "big tree", "kiwi", "art"]

    # 1. Исключить строки с пробелами (то есть оставить те, где пробела НЕТ)
    # [cite: 13]
    no_spaces = filter_strings(lambda s: " " not in s, test_words)
    print(f"Без пробелов: {no_spaces}")

    # 2. Исключить строки, начинающиеся с буквы “a” 
    # (оставляем те, которые НЕ начинаются на 'a') [cite: 14]
    no_start_a = filter_strings(lambda s: not s.lower().startswith("a"), test_words)
    print(f"Не начинаются на 'a': {no_start_a}")

    # 3. Исключить строки, длина которых меньше 5 
    # (оставляем те, длина которых 5 или больше) [cite: 15]
    length_5_plus = filter_strings(lambda s: len(s) >= 5, test_words)
    print(f"Длина 5 и больше: {length_5_plus}")