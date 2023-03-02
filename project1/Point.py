class Point:
    # Constructor
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Accessors
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    # Mutators
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    # String Override
    def __str__(self):
        return "Point: ({}, {})".format(self.get_x(), self.get_y())



