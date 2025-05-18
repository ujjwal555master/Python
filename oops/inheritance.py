class vehicles:

    def __init__(self):
        print("this is  a vehicle ")

    def stop(self):
        print("vehicles start")

    # def stop(self, name):
    #     print(name, "hello")
    # in python method overloading not work as java but we can create by write a logic

class Car(vehicles):

    def start(self):        #method overriding
        print("Car stop")


obj1 = Car()
obj1.start()
obj1.stop()
obj1.stop("ram")


#operator overloading
