#Aggreagation

class Customer:
    
    def __init__(self, name, roll, Address):
        self.name = name
        self.roll = roll
        self.Address = Address

    def changeaddress(self, street, city):
        self.Address.street = street

    

class Addres:
    def __init__(self, street, city):
        self.street = street
        self.city = city
    

objadd = Addres("ramchock", "meerut")
print(id(objadd))
obj = Customer("ram", 123, objadd)
print(obj.Address.street)
obj.changeaddress("rammmmm", "meerut")
print(obj.Address.street)

