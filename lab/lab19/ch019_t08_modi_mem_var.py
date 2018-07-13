class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))


my_car = Car("DeLorean", "silver", 88)
my_car.display_car()
