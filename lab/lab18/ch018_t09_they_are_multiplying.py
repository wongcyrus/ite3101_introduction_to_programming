class Animal(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def description(self):
        print(self.name)
        print(self.age)


hippo = Animal("Peter", 10)
hippo.description()
