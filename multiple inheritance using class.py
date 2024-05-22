class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class worker:
    def __init__(self,job_title):
        self.job_title=job_title

class studentWorker(person, worker):
    def __init__(self, name, age, job_title,student_id):
        person.__init__(self, name, age)
        worker.__init__(self, job_title)
        self.student_id=student_id
        
sw1=studentWorker("John", 25, "Software Engineer", "12345")
print(sw1.name)
print(sw1.age)
print(sw1.job_title)
print(sw1.student_id)