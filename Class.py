## simple class in python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f" student name is {self.name}, the age is {self.age}")  
        
student1 = Student("Fanuel",20)        
student1.display() 
        
## Now on inheritance from class Student
class graduate(Student):
    def __init__(self, name, age, degree):
        super().__init__(name, age) ## calls the parent class constructor
        self.degree = degree
        
    def display(self):
        super().display()  ## calls the parent class method    
        print(f"Degree: {self.degree}")
        
grad_student = graduate("Fanu", 22, "Bachelors in computer science")        
grad_student.display()
        