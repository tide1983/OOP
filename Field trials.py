from typing import List

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

class Reviewer(Person):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.first_name}, Фамилия: {self.last_name}"

class Lecturer(Person):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.courses_attached = []
        self.grades = {}  # Хранится оценка за каждую лекцию (списки оценок по каждому курсу)

    def _calculate_avg_grade(self, course=None):
        """
        Рассчитывает среднюю оценку за лекции.
        Если указан курс, возвращает среднюю оценку только по этому курсу,
        иначе — общую среднюю оценку по всем курсам.
        """
        if course:
            grades = self.grades.get(course, [])
            return sum(grades) / len(grades) if grades else 0
        else:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return f"Имя: {self.first_name}, Фамилия: {self.last_name}, Средняя оценка за лекции: {avg_grade:.1f}"

class Student(Person):
    def __init__(self, first_name: str, last_name: str, gender: str):
        super().__init__(first_name, last_name)
        self.gender = gender
        self.courses_in_progress = []
        self.completed_courses = []
        self.grades = {}  # Оценки за домашние задания по разным курсам

    def _calculate_avg_grade(self, course=None):
        """
        Рассчитывает среднюю оценку за выполнение домашнего задания.
        Если указан курс, возвращает среднюю оценку только по этому курсу,
        иначе — общую среднюю оценку по всем курсам.
        """
        if course:
            grades = self.grades.get(course, [])
            return sum(grades) / len(grades) if grades else 0
        else:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        completed_courses_str = ', '.join(self.completed_courses)
        return (
            f"Имя: {self.first_name}, Фамилия: {self.last_name},\\n"
            f"Средняя оценка за домашние задания: {avg_grade:.1f},\\n"
            f"Курсы в процессе изучения: {courses_in_progress_str},\\n"
            f"Завершенные курсы: {completed_courses_str}"
        )

def count_avg_homework_grade(students: List[Student], course: str) -> float:
    """
    Подсчет средней оценки за домашние задания по конкретному курсу.
    """
    total_grades = []
    for student in students:
        grades_for_course = student.grades.get(course, [])
        total_grades.extend(grades_for_course)
    return sum(total_grades) / len(total_grades) if total_grades else 0

def count_avg_lecture_grade(lecturers: List[Lecturer], course: str) -> float:
    """
    Подсчет средней оценки за лекции по конкретному курсу.
    """
    total_grades = []
    for lecturer in lecturers:
        grades_for_course = lecturer.grades.get(course, [])  # Берем оценки по нужному курсу
        total_grades.extend(grades_for_course)               # Собираем все оценки в один список
    return sum(total_grades) / len(total_grades) if total_grades else 0

# Экземпляры классов
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Анна', 'Петрова')

student1 = Student('Руслан', 'Ахметов', 'Мужской')
student2 = Student('Марина', 'Семенова', 'Женский')

# Назначение курсов
lecturer1.courses_attached = ['Python', 'JavaScript']
lecturer2.courses_attached = ['Python', 'Ruby']

student1.courses_in_progress = ['Python', 'JavaScript']
student1.completed_courses = ['Введение в IT']

student2.courses_in_progress = ['Python', 'Ruby']
student2.completed_courses = ['Основы программирования']

# Оценки за домашние задания
student1.grades['Python'] = [9, 8, 10]
student1.grades['JavaScript'] = [7, 9]

student2.grades['Python'] = [8, 9, 9]
student2.grades['Ruby'] = [7, 8]

# Оценки за лекции
lecturer1.grades['Python'] = [9, 8, 10]
lecturer1.grades['JavaScript'] = [7, 9]

lecturer2.grades['Python'] = [8, 9, 9]
lecturer2.grades['Ruby'] = [7, 8]

# Список студентов и лекторов
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

# Подсчет средней оценки за домашние задания по курсу Python
avg_hw_grade = count_avg_homework_grade(students, 'Python')
print(f"\\nСредняя оценка за домашние задания по курсу Python: {avg_hw_grade:.1f}")

# Подсчет средней оценки за лекции по курсу Python
avg_lec_grade = count_avg_lecture_grade(lecturers, 'Python')
print(f"Средняя оценка за лекции по курсу Python: {avg_lec_grade:.1f}")

# Информация обо всех созданных объектах
print("\\nИнформация о преподавателях:")
for lecturer in lecturers:
    print(lecturer)

print("\\nИнформация о студентах:")
for student in students:
    print(student)


