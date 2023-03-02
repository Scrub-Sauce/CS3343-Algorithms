class Line:
    # Constructor
    def __init__(self, starting_point, ending_point):
        self._starting_point = starting_point
        self._ending_point = ending_point

    # Accessors
    def get_starting_point(self):
        return self._starting_point

    def get_ending_point(self):
        return self._ending_point

    # Mutators
    def set_starting_point(self, starting_point):
        self._starting_point = starting_point

    def set_ending_point(self, ending_point):
        self._ending_point = ending_point

    # String Override
    def __str__(self):
        return "Line - Starting {} Ending {}".format(self.get_starting_point(), self.get_ending_point())
