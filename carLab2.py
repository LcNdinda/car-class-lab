class Car:
    def __init__(self, type, model, name):
        self.type = type
        self.model = model
        self.name = name

    def car_description(self):
        # print("Your car is a: {} {} {}".format(self.type, self.model, self.name))
        # print("Your car is a: {} {} {}".format(self.type, self.model, self.name))
          print("Your car is a: ", self.type)

car1 = Car("Toyota", "vitz", "KAR")
car1.carDescription()
