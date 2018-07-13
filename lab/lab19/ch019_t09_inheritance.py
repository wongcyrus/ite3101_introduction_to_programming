class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print("This is a % s % swith % s MPG." % (self.color, self.model, str(self.mpg)))

    def drive_car(self):
        self.condition = "used"
