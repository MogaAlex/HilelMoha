class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name


    def __str__(self):
        return f'{self.gender} {self.age} {self.first_name} {self.last_name}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f'{self.gender} {self.age} {self.first_name} {self.last_name} {self.record_book}'

# Код для домашней работы 14.1
class manystudents(Exception):
    pass

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.count = 0

    def add_student(self, student):
        self.group.add(student)

        self.count += 1
        if self.count > 10:
            raise manystudents("Больше десяти")
        # -------------------------------------------------------------------------------------------
    def Error(self):
        pass

    def delete_student(self, last_name):
        for student in list(self.group):
            if last_name in student.last_name:
                self.group.remove(student)
            else:
                None

    def find_student(self, last_name):
        for student in self.group:
            if last_name in student.last_name:
                return student
            else:
                None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f'{student.first_name} {student.last_name} {student.age} {student.gender} {student.record_book}\n'
        return f'Number:{self.number}\n{all_students} '



st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 25, 'Liza2312', 'Taylor', 'AN145')
st4 = Student('Female', 25, 'Lizafds', 'Taylor', 'AN145')
st5 = Student('Female', 25, 'Lizabg', 'Taylor', 'AN145')
st6 = Student('Female', 25, 'Lizaa', 'Taylor', 'AN145')
st7 = Student('Female', 25, 'Lizas', 'Taylor', 'AN145')
st8 = Student('Female', 25, 'Lizahty', 'Taylor', 'AN145')
st9 = Student('Female', 25, 'Lizafe', 'Taylor', 'AN145')
st10 = Student('Female', 25, 'Liza6h5h', 'Taylor', 'AN145')
st11 = Student('Female', 25, 'Lizargege', 'Johnson', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)


print(gr)

try:
    gr.add_student(st11)
except manystudents as e:
    print(e)

