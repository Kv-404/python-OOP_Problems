class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks  

    def average(self):
        total = 0
        for m in self.marks:
            total += m
        return total / len(self.marks)


name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = list(map(float, input("Enter marks separated by space: ").split()))

student = Student(name, roll, marks)

print("Average Marks:", student.average())
