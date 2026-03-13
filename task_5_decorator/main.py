import time

# Тот самый декоратор
def execution_timer(func):
    """Декоратор, который выводит в консоль время выполнения декорируемой функции."""
    def wrapper(*args, **kwargs):
        start_time = time.time()          # Засекаем время до
        result = func(*args, **kwargs)    # Вызываем саму функцию
        end_time = time.time()            # Засекаем время после
        
        # Вычисляем разницу и выводим
        execution_time = end_time - start_time
        print(f"[{func.__name__}] Время выполнения: {execution_time:.6f} сек.")
        
        return result
    return wrapper

# Первая функция (просто сумма в консоль)
@execution_timer
def sum_and_print(a: float, b: float):
    """Вычисляет сумму двух чисел a и b, выводит результат в консоль."""
    result = a + b
    print(f"Сумма {a} + {b} = {result}")
    return result

# Вторая функция (работа с файлами)
@execution_timer
def sum_from_file(input_file: str, output_file: str):
    """Читает из файла два числа, записывает сумму в другой файл."""
    # Читаем данные
    with open(input_file, 'r', encoding='utf-8') as f:
        # Считываем весь текст и разбиваем по пробелам/переносам строк
        data = f.read().split()
        if len(data) >= 2:
            a = float(data[0])
            b = float(data[1])
        else:
            print("Ошибка: в файле недостаточно данных!")
            return

    # Вычисляем сумму
    result = a + b

    # Записываем результат
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(result))
    
    print(f"Результат ({result}) успешно записан в файл {output_file}")


# --- Проверка работы кода ---
if __name__ == "__main__":
    print("--- Тест первой функции ---")
    sum_and_print(10.5, 20.2)
    
    print("\n--- Тест второй функции ---")
    # Передаем названия наших файлов
sum_from_file('task_5_decorator/input.txt', 'task_5_decorator/output.txt')