from Point import Point
from Line import Line
import matplotlib.pyplot as plt
import sys


class Plot:
    _instance = None

    def __init__(self):
        self._points = []
        self._lines = []
        self._convex_hull = []
        if Plot._instance is not None:
            raise Exception("Plot is a singleton and can only be initiated once")
        Plot._instance = self

    # Get Plot Singleton
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
        try:
            with open(filename) as file:
                rows = file.readlines()
                for row in rows:
                    coordinates = row.split(',')
                    tmp_point = Point(float(coordinates[0]), float(coordinates[1].strip('\n')))
                    self.get_points().append(tmp_point)
        except FileNotFoundError:
            sys.stderr.write(
                "Error: The file '{}' does not exist. The file must be in the same directory as 'main.py'".format(
                    filename))
            sys.exit(1)

    def add_point(self, point):
        self.get_points().append(point)

    def remove_point(self, point):
        self.get_points().remove(point)

    def add_line(self, point_a, point_b):
        tmp_line = Line(point_a, point_b)
        self.get_lines().append(tmp_line)

    def remove_line(self, line):
        self.get_lines().remove(line)

    def add_convex_hull(self, point):
        self.get_convex_hull().append(point)

    def remove_convex_hull(self, point):
        self.get_convex_hull().remove(point)

    # Create Scatter Plot
    def create_scatter_plot(self):
        plt.scatter([point._x for point in self.get_points()], [point._y for point in self.get_points()])
        plt.plot([point._x for point in self.get_convex_hull()], [point._y for point in self.get_convex_hull()])
        plt.show()

    # Find Convex Hull
    def find_convex_hull(self):
        return

    # String Override
    def __str__(self):
        ret = 'Scatter Plot\n----------------------------------\nPoints\n----------------------------------\n'
        for point in self.get_points():
            ret += "{}\n".format(point)
        ret += "----------------------------------\nLines\n----------------------------------\n"
        for line in self.get_lines():
            ret += "{}\n".format(line)
        ret += "----------------------------------\nConvex Hull Points\n----------------------------------\n"
        for convex_hull in self.get_convex_hull():
            ret += "{}\n".format(convex_hull)
        return ret
