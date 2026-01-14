class Student:
    def __init__(self, name):
        self.name = name
        self.grade = None

    def view_grade(self):
        print(self.grade)


class Teacher:
    def __init__(self, name):
        self.name = name

    def assign_grade(self, student, grade):
        student.grade = grade
