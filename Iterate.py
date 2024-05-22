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

people=[
    Employee("John", 30, "E0001"),
    Student("Jane", 20, "S0001"),
    Employee("Bob", 40, "E0002"),
    Student("Alice", 25, "S0002")
]

for person in people:
    print(f"Name: {person.name}, Age: {person.age}")
    if isinstance(person, Employee):
        print(f"{person.name} is an employee with ID {person.employee_id}")
    elif isinstance(person, Student):
        print(f"{person.name} is a student with ID {person.student_id}")
    else:
        print(f"{person.name} is a person with unknown ID")

