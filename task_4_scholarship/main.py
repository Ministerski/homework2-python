class Student:
    def __init__(self, full_name: str, age: int, group_number: str, average_grade: float):
        # Базовые свойства студента [cite: 21, 23]
        self.full_name = full_name
        self.age = age
        self.group_number = group_number
        self.average_grade = average_grade

    def get_info(self) -> str:
        """Выводит информацию о человеке (фио, возраст) """
        return f"ФИО: {self.full_name}, Возраст: {self.age}"

    def get_scholarship(self) -> int:
        """Вычисляет размер стипендии студента """
        if self.average_grade == 5.0:
            return 6000
        elif self.average_grade >= 4.0: # Считаем, что "меньше 5" - это от 4 до 4.9
            return 4000
        else:
            return 0 # В других случаях (меньше 4) 

    def compare_scholarship(self, other: 'Student') -> str:
        """Сравнивает стипендию с другим студентом/аспирантом """
        my_scholarship = self.get_scholarship()
        other_scholarship = other.get_scholarship()
        
        if my_scholarship > other_scholarship:
            return f"У {self.full_name} стипендия больше ({my_scholarship}р vs {other_scholarship}р)"
        elif my_scholarship < other_scholarship:
            return f"У {self.full_name} стипендия меньше ({my_scholarship}р vs {other_scholarship}р)"
        else:
            return f"У {self.full_name} и {other.full_name} стипендии равны ({my_scholarship}р)"


class Aspirant(Student):
    def __init__(self, full_name: str, age: int, group_number: str, average_grade: float, science_work: str):
        # Вызываем __init__ родительского класса, чтобы не писать всё заново
        super().__init__(full_name, age, group_number, average_grade)
        # Добавляем уникальное свойство аспиранта 
        self.science_work = science_work

    def get_scholarship(self) -> int:
        """Переопределяем размер стипендии для аспиранта """
        if self.average_grade == 5.0:
            return 8000
        elif self.average_grade >= 4.0:
            return 6000
        else:
            return 0


# --- Проверка работы кода ---
if __name__ == "__main__":
    # Создаем обычных студентов
    student1 = Student("Иванов Иван Иванович", 20, "БИ-21", 5.0)
    student2 = Student("Петров Петр Петрович", 21, "БИ-21", 4.2)
    student3 = Student("Сидоров Сидор", 19, "БИ-22", 3.5)

    # Создаем аспирантов
    aspirant1 = Aspirant("Смирнов Алексей", 25, "АСП-1", 5.0, "Исследование ИИ")
    aspirant2 = Aspirant("Козлов Дмитрий", 24, "АСП-1", 4.8, "Квантовые вычисления")

    # Проверяем методы
    print(student1.get_info())
    print(aspirant1.get_info())
    print("-" * 20)
    
    print(f"Стипендия отличника студента: {student1.get_scholarship()}р")
    print(f"Стипендия хорошиста студента: {student2.get_scholarship()}р")
    print(f"Стипендия троечника студента: {student3.get_scholarship()}р")
    print(f"Стипендия отличника аспиранта: {aspirant1.get_scholarship()}р")
    print("-" * 20)

    # Сравниваем
    print(student1.compare_scholarship(student2))
    print(student2.compare_scholarship(aspirant2))
    print(aspirant1.compare_scholarship(student1))