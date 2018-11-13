class Vehicle:
    name = ""
    model = ""
    type = ""
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a model: %s, of type: %s, color: %s, worth $%.2f" %(self.name, self.model, self.type, self.color, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Ferari"
car1.model = "runner"
car1.type = "convertible"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jaguar"
car1.model = "runner"
car1.type = "van"
car2.color = "Blue"
car2.value = 10000.00

print(car1.description())
print(car2.description())
