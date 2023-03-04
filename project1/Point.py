class Point:
    # Constructor
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._counter_next = None
        self._clock_next = None

    # Accessors
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_counter_next(self):
        return self._counter_next

    def get_clock_next(self):
        return self._clock_next

    # Mutators
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_counter_next(self, counter_next):
        self._counter_next = counter_next

    def set_clock_next(self, clock_next):
        self._clock_next = clock_next

    # String Override
    def __str__(self):
        return 'Point: ({}, {})'.format(self.get_x(), self.get_y())
