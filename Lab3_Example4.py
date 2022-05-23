# LSGI3315 Lab 3 20016345D - Example 4: The Argument "self" in Class Definition
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add_twice(self, x):
        self.add(x)
        self.add(x)
