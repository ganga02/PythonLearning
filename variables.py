class Car:
    wheels = 4
    def __init__(self):
        self.mil=8
        self.company = "BMW"

c1 = Car()
c2 = Car()
# we can access class variable by using ClassName or ObjectName
print(Car.wheels) #Here we are accessing class variable by using ClassName

Car.wheels = 5 #Modifying class variable using class Name

c1.mil=15

print(c1.mil,c1.company,c1.wheels)#Here we are accessing class variable using ObjectName
print(c2.mil,c2.company,c2.wheels)