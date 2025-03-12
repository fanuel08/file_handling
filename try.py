## a class
class Parent:
    def __init__(self, name, age, number):
        self.name = name
        self.age  = age
        self.number = number
        
    def show(self):
        print(f"The parent name is: {self.name}, the age: {self.age}, the number: {self.number}")
        
parent = Parent("Matthew", 54, "+234-779-56776")
parent.show()       

## Inheritance from a class Parent
class Child(Parent):
    def __init__(self, name, age, number, stream):
        super().__init__(name, age, number)
        self.stream = stream
        
    def show(self):
        super().show() # calls the parent class method
        print(f"The child stream is: {self.stream}")    
         
child = Child("Mark", 22, "+234-34564-786", "2 West") 
child.show()        