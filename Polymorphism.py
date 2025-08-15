class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Reviewer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.first_name}\\nФамилия: {self.last_name}"

class Lecturer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.courses_attached = []
        self.grades = {}  # Хранилище оценок по курсам (ключ — курс, значение — список оценок)

    def _calculate_avg_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        return 0

    def __lt__(self, other):
        avg_self = self._calculate_avg_grade()
        avg_other = other._calculate_avg_grade()
        return avg_self < avg_other

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return (
            f"Имя: {self.first_name}\\n"
            f"Фамилия: {self.last_name}\\n"
            f"Средняя оценка за лекции: {avg_grade:.1f}"
        )

class Student(Person):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name)
        self.gender = gender
        self.courses_in_progress = []
        self.completed_courses = []
        self.grades = {}  # Хранилище оценок по курсам (ключ — курс, значение — список оценок)

    def _calculate_avg_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        return 0

    def __lt__(self, other):
        avg_self = self._calculate_avg_grade()
        avg_other = other._calculate_avg_grade()
        return avg_self < avg_other

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        completed_courses_str = ", ".join(self.completed_courses)
        return (
            f"Имя: {self.first_name}\\n"
            f"Фамилия: {self.last_name}\\n"
            f"Средняя оценка за домашние задания: {avg_grade:.1f}\\n"
            f"Курсы в процессе изучения: {courses_in_progress_str}\\n"
            f"Завершенные курсы: {completed_courses_str}"
        )

# Демонстрационный пример
lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.grades['Python'] = [9, 9, 10]
lecturer1.grades['Git'] = [8, 9]

lecturer2 = Lecturer('Other', 'Teacher')
lecturer2.grades['Python'] = [7, 8, 9]
lecturer2.grades['Math'] = [8, 9]

student1 = Student('Ruoy', 'Eman', 'Мужской')
student1.grades['Python'] = [9, 9, 10]
student1.grades['Git'] = [8, 9]
student1.courses_in_progress = ['Python', 'Git']
student1.completed_courses = ['Введение в программирование']

student2 = Student('Jane', 'Doe', 'Женский')
student2.grades['Python'] = [7, 8, 9]
student2.grades['Math'] = [8, 9]
student2.courses_in_progress = ['Python', 'Math']
student2.completed_courses = ['Основы программирования']

# Печать объектов
print("\\nИнформация о проверяющем:")
print(Reviewer('Check', 'Me'))

print("\\nИнформация о первом лекторе:")
print(lecturer1)

print("\\nИнформация о втором лекторе:")
print(lecturer2)

print("\\nИнформация о первом студенте:")
print(student1)

print("\\nИнформация о втором студенте:")
print(student2)

# Сравнения
print("\\nСравниваем лекторов:")
print(f"{lecturer1.first_name} лучше {lecturer2.first_name}: {lecturer1 > lecturer2}")

print("\\nСравниваем студентов:")
print(f"{student1.first_name} лучше {student2.first_name}: {student1 > student2}")