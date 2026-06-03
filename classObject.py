class Computer:
    def config(self):
        print("Ganga")


comp1 = Computer()
comp2 = Computer()

print(type(comp1))

Computer.config(comp1)
Computer.config(comp2)

comp1.config()
comp2.config()