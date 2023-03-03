from Plot import Plot
from Line import Line
from Point import Point
import math
import sys


def find_convex_hull(points):
    n = len(points)

    if n <= 3:
        if n == 2:
            return points
        elif n == 3:
            tmp_line = Line(points[0], points[1])
            if tmp_line.point_above_line(points[2]):
                points[1], points[2] = points[2], points[1]
            return points

    # Recursively call this function till we hit our base case
    left_convex_hull = find_convex_hull(points[0:math.ceil(n / 2)])
    right_convex_hull = find_convex_hull(points[math.ceil(n / 2) + 1:n])

    merge_convex_hull(left_convex_hull, right_convex_hull)


def merge_convex_hull(self, left_convex, right_convex):
    left_position = left_convex[len(left_convex - 1)]
    right_position = right_convex[0]

    left_min = min(left_convex, key=lambda point: point.get_y())
    right_min = min(right_convex, key=lambda point: point.get_y())
    # lower_tangent =


if __name__ == "__main__":
    if len(sys.argv) == 1:
        in_file = "input.csv"
    elif len(sys.argv) == 2:
        in_file = sys.argv[1]
    else:
        sys.stderr.write(
            "Invalid usage: 'python3 main.py' (Assumes input file is named 'input.csv') or 'python3 main.py [filename]'")
        sys.exit(1)

    scatter_plot = Plot.get_plot_instance()
    scatter_plot.populate(in_file)
    print(scatter_plot)
    scatter_plot.create_scatter_plot()

    firstPoint = Point(2, 4)
    secondPoint = Point(2, 2)
    myLine = Line(firstPoint, secondPoint)

    testPoint = Point(3, 3)
    print(myLine)

    myLine.set_starting_point(testPoint)
    print(myLine)
