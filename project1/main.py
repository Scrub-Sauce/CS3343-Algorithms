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
            if not tmp_line.point_above_line(points[2]):
                tmp_points = [points[0], points[2], points[1]]
                return tmp_points
            else:
                return points
    else:
        left_points = points[0:math.ceil(n / 2)]
        right_points = points[math.ceil(n / 2):]
        left_convex_hull = find_convex_hull(left_points)
        right_convex_hull = find_convex_hull(right_points)

        return merge_convex_hull(left_convex_hull, right_convex_hull)


def merge_convex_hull(left_convex, right_convex):

    lower_tangent = find_lower_hull(left_convex, right_convex)
    upper_tangent = find_upper_hull(left_convex, right_convex)

    start = left_convex.index(upper_tangent.get_starting_point())
    next_left_index = (start - 1) % len(left_convex)
    while True:
        if left_convex[next_left_index] == lower_tangent.get_starting_point():
            break
        left_convex.remove(left_convex[next_left_index])
        next_left_index = (next_left_index - 1) % len(left_convex)

    start = right_convex.index(upper_tangent.get_ending_point())
    next_right_index = (start + 1) % len(right_convex)
    while True:
        if right_convex[next_right_index] == lower_tangent.get_ending_point():
            break
        right_convex.remove(right_convex[next_right_index])
        next_right_index = (next_right_index + 1) % len(right_convex)

    return left_convex + right_convex


def find_lower_hull(left_convex, right_convex):
    left_index = len(left_convex) - 1
    right_index = 0
    lower_tangent = Line(left_convex[left_index], right_convex[right_index])

    lower_hull_found = False

    while not lower_hull_found:
        next_left_index = (left_index - 1) % len(left_convex)
        while not lower_tangent.point_above_line(left_convex[next_left_index]):
            lower_tangent.set_starting_point(left_convex[next_left_index])
            next_left_index = (next_left_index - 1) % len(left_convex)

        next_right_index = (right_index + 1) % len(right_convex)
        while not lower_tangent.point_above_line(right_convex[next_right_index]):
            lower_tangent.set_ending_point(right_convex[next_right_index])
            next_right_index = (next_right_index + 1) % len(right_convex)

        if lower_tangent.point_above_line(left_convex[next_left_index]):
            lower_hull_found = True

    return lower_tangent


def find_upper_hull(left_convex, right_convex):
    left_index = len(left_convex) - 1
    right_index = 0
    upper_tangent = Line(left_convex[left_index], right_convex[right_index])

    upper_hull_found = False

    while not upper_hull_found:
        next_left_index = (left_index + 1) % len(left_convex)
        while upper_tangent.point_above_line(left_convex[next_left_index]):
            upper_tangent.set_starting_point(left_convex[next_left_index])
            next_left_index = (next_left_index + 1) % len(left_convex)

        next_right_index = (right_index - 1) % len(right_convex)
        while upper_tangent.point_above_line(right_convex[next_right_index]):
            upper_tangent.set_ending_point(right_convex[next_right_index])
            next_right_index = (next_right_index - 1) % len(right_convex)

        if not upper_tangent.point_above_line(left_convex[next_left_index]):
            upper_hull_found = True

    return upper_tangent


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
    scatter_plot.set_convex_hull(find_convex_hull(scatter_plot.get_points()))
    scatter_plot.create_scatter_plot()
    print(scatter_plot)
