#constructor is like a function used in class and invoke automatically when you creating an object.
#it's take self parameter which refrence of objects
#consturctor is define by using __init__()

class Car:
    company = 'Mercedes'  #Define which is similar to the all objects
    def __init__(self, fullname):
        self.name = fullname

obj1 = Car('Ram babu')
print(obj1.name)


#Abstraction : hiding the implementation details and only see essintial to user
class Car2:
    def __init__(self):
        self.breaks = False
        self.acc = False
        self.clutch = False

    def start(self):
        self.clutch = True          #this details hide alll thing and see only that car started
        self.acc = True
        print('CarStarted....')

obj2 = Car2()
obj2.start()


#Encapsulation = wrapping the data and function into a single unit(object)