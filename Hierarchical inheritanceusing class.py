class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

e1 = Employee("Alice", 30, "E123")
s1 = Student("Bob", 20, "S456")

print(e1.name)
print(e1.age)
print(e1.employee_id)

print(s1.name)
print(s1.age)
print(s1.student_id)
