from Point import Point


class Plot:
    _instance = None

    def __init__(self):
        self._points = []
        self._lines = []
        self._convex_hull = []
        if Plot._instance is not None:
            raise Exception("Plot is a singleton and can only be initiated once")
        Plot._instance = self

    # Get Singleton
    @staticmethod
    def get_plot_instance():
        if Plot._instance is None:
            Plot()
        return Plot._instance

    # Accessors
    def get_points(self):
        return self._points

    def get_lines(self):
        return self._lines

    def get_convex_hull(self):
        return self._convex_hull

    # Mutators
    def set_points(self, points):
        self._points = points

    def set_lines(self, lines):
        self._lines = lines

    def set_convex_hull(self, convex_hull):
        self._convex_hull = convex_hull

    # Populate - Populated the scatter plot from the CSV provided.
    def populate(self, filename):
        with open(filename) as file:
            rows = file.readlines()
            for row in rows:
                coordinates = row.split(',')
                tmp_point = Point(coordinates[0], coordinates[1])
                self.get_points().append(tmp_point)

    # String Override
    def __str__(self):
        ret = 'Scatter Plot\n----------------------------------\nPoints\n----------------------------------\n'
        for point in self.get_points():
            ret += "{}".format(point)
        ret += "----------------------------------\nLines\n----------------------------------\n"
        for line in self.get_lines():
            ret += "{}".format(line)
        ret += "----------------------------------\nConvex Hull Points\n----------------------------------\n"
        for point in self.get_convex_hull():
            ret += "{}".format(point)
        return ret
