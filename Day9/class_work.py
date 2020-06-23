"""ООП В ПИТОНЕ CLASS И Т.Д"""


class Person:
    def __init__(self, firstname, lastname, surname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.surname = surname
        self.age = age
        self.person = []
        self.subject = []
        self.item = []


class Teacher(Person):

    def students(self):
        print(self.person)

    @property
    def student(self):
        return self.student

    @student.setter
    def student(self, student):
        result = {
            "name": student.firstname,
            "lastname": student.lastname,
            'surname': student.surname,
            'age': student.age
        }
        self.person.append(result)


class Student(Person):
    def teachers(self):
        print(self.person)

    @property
    def teacher(self):
        return self.teacher

    @teacher.setter
    def teacher(self, teacher):
        result = {"name": teacher.firstname,
                  "lastname": teacher.lastname,
                  "surname": teacher.surname,
                  "age": teacher.age}
        self.person.append(result)


t1 = Teacher('Bob', 'Criss', 'Petrovich', 34)
t2 = Teacher('Anna', 'Tips', 'Ivanovna', 34)
s1 = Student('Tod', 'sadasd', 'Vasya', 12)
s2 = Student('Sam', 'Kitushi', 'Gogol', 15)

t1.student = s1
t1.student = s2

t1.students()
s.teacher = t
s.teachers()
