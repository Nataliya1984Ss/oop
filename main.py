class Student:
    def __init__(self, name, surname, grades, finished_courses,courses_in_progress):
        self.name = name
        self.surname = surname

        self.finished_courses = finished_courses
        self.courses_in_progress = courses_in_progress
        self.grades = grades
    def rate_lk(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания:{self.grades}\nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}"
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades
    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{self.grades}"
class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}"


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# some_reviewer = Reviewer('Some', 'Buddy')
# some_lecturer = Lecturer ('Some', 'Buddy', '9.9')
# some_student = Student ('Ruoy', 'Eman', '9.9', 'Python, Git','Введение в программирование')
# print(some_reviewer)
# print(some_lecturer)
# print(some_student)

def __eq__(self, other):
    if not isinstance(other, (int, Student)):
        raise TypeError
    sc = other if isinstance(other, int) else other.grades
    return self.grades == sc

def __eq__(self, other):
    if not isinstance(other, (int, Lecturer)):
        raise TypeError

    sc = other if isinstance(other, int) else other.grades
    return self.grades == sc
a = {'Python': [4,4,5]}
b = {'Python': [4,5,5]}
print (a==b)