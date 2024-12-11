# Задача 1:
class Teacher:
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience
        self._marks = {}

    def get_name(self):
        return self._name

    def get_education(self):
        return self._education

    def get_experience(self):
        return self._experience

    def set_experience(self, experience):
        if experience >= 0:
            self._experience = experience
        else:
            raise ValueError("Опыт работы не может быть отрицательным")

    def get_teacher_data(self):
        return {
            "Имя": self._name,
            "Образование": self._education,
            "Опыт работы": self._experience
        }

    def add_mark(self, student_name, mark):
        if student_name in self._marks:
            self._marks[student_name].append(mark)
        else:
            self._marks[student_name] = [mark]

    def remove_mark(self, student_name, mark):
        if student_name in self._marks and mark in self._marks[student_name]:
            self._marks[student_name].remove(mark)

    def give_a_consultation(self, class_name):
        return f"Консультация проведена для класса {class_name}"


# Задача 2:
class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self._discipline = discipline
        self._job_title = job_title

    def get_discipline(self):
        return self._discipline

    def get_job_title(self):
        return self._job_title

    def set_job_title(self, job_title):
        self._job_title = job_title

    def get_teacher_data(self):
        data = super().get_teacher_data()
        data["Дисциплина"] = self._discipline
        data["Должность"] = self._job_title
        return data

    def give_a_consultation(self, class_name):
        return f"{self._discipline} учитель провел консультацию для класса {class_name}"

teacher = Teacher("Иван Петров", "БГПУ", 4)

print(teacher.get_teacher_data())  # Информация об учителе
teacher.add_mark("Алексей", 5)
teacher.add_mark("Алексей", 4)
teacher.remove_mark("Алексей", 5)
print(teacher._marks)  # Проверка оценок
print(teacher.give_a_consultation("10А"))  # Консультация


discipline_teacher = DisciplineTeacher("Мария Иванова", "МГУ", 10, "Математика", "Завуч")

print(discipline_teacher.get_teacher_data())  # Информация о преподавателе дисциплины
print(discipline_teacher.give_a_consultation("11Б"))