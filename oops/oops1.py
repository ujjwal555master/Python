# creating the class

class Student:
    name='king'
    def greet(self):                #method defining
        print(f'hello, {self.name}')

class Student2:
    #creating an static method:- A method which not cantain self patameter
    @staticmethod     #decorator
    def college():
        print('hello students')

# creating an objects
obj1 = Student()
obj2 = Student()
print(obj1.name)
obj1.greet()

obj1.name = 'changename'
print(obj1.name)


#static method 
Student2.college()      #level of class
obj3 = Student2()       #level of objects
obj3.college()