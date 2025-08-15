class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Student(Person):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name)
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}  # Это для будущих оценок по домашним работам, но пока пусто

    def rate_lecture(self, lecturer, course, grade):
        """
        Поставить оценку преподавателю за проведенную лекцию.
        Возвращает строку с результатом операции.
        """
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if hasattr(lecturer, 'grades'):
                lecturer.grades.setdefault(course, []).append(grade)
                return f"Оценка {grade} успешно поставлена лектору {lecturer.first_name} {lecturer.last_name}"
            else:
                return "Ошибка: Неправильный объект лектора"
        else:
            return "Ошибка: Невозможно поставить оценку"

class Lecturer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.courses_attached = []
        self.grades = {}  # Словарь для хранения оценок по курсам

class Reviewer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.courses_attached = []

# Создание объектов участников
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёшина', 'Ольга', 'Ж')

# Добавление курсов участникам
student.courses_in_progress.extend(['Python', 'Java'])
lecturer.courses_attached.extend(['Python', 'C++'])
reviewer.courses_attached.extend(['Python', 'C++'])

# Проверка метода выставления оценок
print(student.rate_lecture(lecturer, 'Python', 7))   # Оценка должна быть принята
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка, потому что Иван Иванов не ведет Java
print(student.rate_lecture(lecturer, 'C++', 8))      # Ошибка, потому что Ольга Алёшина не учится на C++
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка, потому что рецензент Пётр Петров не принимает оценки

# Выведем итоговые оценки Ивана Иванова
print(lecturer.grades)  # Должно вернуть {'Python': [7]}
