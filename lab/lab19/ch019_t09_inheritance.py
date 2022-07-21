class Car(object):

    def __init__(self, model: str, color: str, mpg: int):
        self.condition = "new"
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print("This is a % s % swith % s MPG." %
              (self.color, self.model, str(self.mpg)))

    def drive_car(self):
        self.condition = "used"
