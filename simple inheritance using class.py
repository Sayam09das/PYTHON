class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no=roll_no

s1=student("sai", 20, "1")
print(s1.name)
print(s1.age)
print(s1.roll_no)