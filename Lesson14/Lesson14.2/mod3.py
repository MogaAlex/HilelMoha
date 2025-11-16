class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)


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