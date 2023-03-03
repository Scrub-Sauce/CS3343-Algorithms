class Line:
    # Constructor
    def __init__(self, starting_point, ending_point):
        self._slope = None
        self._y_intercept = None
        self._is_vertical = None
        self._starting_point = starting_point
        self._ending_point = ending_point
        self.update_properties()

    # Accessors
    def get_starting_point(self):
        return self._starting_point

    def get_ending_point(self):
        return self._ending_point

    def get_slope(self):
        return self._slope

    def get_y_intercept(self):
        return self._y_intercept

    def get_is_vertical(self):
        return self._is_vertical

    # Mutators
    def set_starting_point(self, starting_point):
        self._starting_point = starting_point
        self.update_properties()

    def set_ending_point(self, ending_point):
        self._ending_point = ending_point
        self.update_properties()

    def set_slope(self):
        if self.get_is_vertical():
            self._slope = None
        else:
            self._slope = (self.get_ending_point().get_y() - self.get_starting_point().get_y()) / (
                    self.get_ending_point().get_x() - self.get_starting_point().get_x())

    def set_y_intercept(self):
        if self.get_is_vertical():
            self._y_intercept = None
        else:
            self._y_intercept = self.get_starting_point().get_y() - (
                        self.get_slope() * self.get_starting_point().get_x())

    def set_is_vertical(self):
        self._is_vertical = (self.get_starting_point().get_x() == self.get_ending_point().get_x())

    def point_above_line(self, point):
        if self.get_is_vertical():
            return False
        else:
            calc_line_y = (self.get_slope() * point.get_x()) + self.get_y_intercept()
            return point.get_y() > calc_line_y

    def update_properties(self):
        self.set_is_vertical()
        self.set_slope()
        self.set_y_intercept()

    # String Override
    def __str__(self):
        return "Line - Starting {}, Ending {}, Slope: {}, Y-Intercept: {}, Vertical: {}".format(
            self.get_starting_point(), self.get_ending_point(), self.get_slope(), self.get_y_intercept(),
            self.get_is_vertical())
