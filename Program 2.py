class Student:
    def __init__(self, name, roll_number, subjects, marks):
        self.name = name
        self.roll_number = roll_number
        self.subjects = subjects
        self.marks = marks

    def calculate_grade(self):
        average_marks = sum(self.marks) / len(self.marks)

        if average_marks >= 90:
            return 'A'
        elif 80 <= average_marks < 90:
            return 'B'
        elif 70 <= average_marks < 80:
            return 'C'
        elif 60 <= average_marks < 70:
            return 'D'
        else:
            return 'F'


student_instance = Student(
    name="Alice",
    roll_number="12345",
    subjects=["Math", "English", "Science"],
    marks=[85, 92, 78]
)


print(f"Student Name: {student_instance.name}")
print(f"Roll Number: {student_instance.roll_number}")
print(f"Subjects: {', '.join(student_instance.subjects)}")
print(f"Marks: {', '.join(map(str, student_instance.marks))}")
print(f"Grade: {student_instance.calculate_grade()}")
