class Computer:
    def __init__(self,cpu,ram): #Constructor
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Computer has",self.cpu,self.ram)


comp1 = Computer('i8',16)
comp2 = Computer('Ryzen',8)

comp1.config()
comp2.config()