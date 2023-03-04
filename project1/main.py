from Plot import Plot
from Line import Line
from Point import Point
import math
import sys


def find_convex_hull(points):
    n = len(points)

    if n <= 3:
        if n == 2:
            points[0].set_clock_next(points[1])
            points[0].set_counter_next(points[1])

            points[1].set_clock_next(points[0])
            points[1].set_counter_next(points[0])

            tmp_scatter_plot = Plot.get_plot_instance()
            tmp_scatter_plot.set_convex_hull(points)
            tmp_scatter_plot.create_scatter_plot()
            return points
        elif n == 3:
            tmp_line = Line(points[0], points[1])
            if tmp_line.point_above_line(points[2]):
                points[0].set_clock_next(points[2])
                points[1].set_clock_next(points[0])
                points[2].set_clock_next(points[1])

                points[0].set_counter_next(points[1])
                points[1].set_counter_next(points[2])
                points[2].set_counter_next(points[0])
            else:
                points[0].set_clock_next(points[1])
                points[1].set_clock_next(points[2])
                points[2].set_clock_next(points[0])

                points[0].set_counter_next(points[2])
                points[1].set_counter_next(points[0])
                points[2].set_counter_next(points[1])

            visual = points
            visual.append(points[0])
            tmp_scatter_plot = Plot.get_plot_instance()
            tmp_scatter_plot.set_convex_hull(visual)
            tmp_scatter_plot.create_scatter_plot()
            return points

    else:
        left_points = points[0:math.ceil(n / 2)]
        right_points = points[math.ceil(n / 2):]
        left_convex_hull = find_convex_hull(left_points)
        right_convex_hull = find_convex_hull(right_points)

        return merge_convex_hull(left_convex_hull, right_convex_hull)


def merge_convex_hull(left_convex, right_convex):
    lower_tangent = find_lower_tan(left_convex, right_convex)
    upper_tangent = find_upper_tan(left_convex, right_convex)

    merged_convex = []

    lower_tangent.get_starting_point().set_counter_next(lower_tangent.get_ending_point())
    lower_tangent.get_ending_point().set_clock_next(lower_tangent.get_starting_point())
    upper_tangent.get_starting_point().set_clock_next(upper_tangent.get_ending_point())
    upper_tangent.get_ending_point().set_counter_next(upper_tangent.get_starting_point())

    starting_point = left_convex[0]
    merged_convex.append(starting_point)
    current_point = starting_point.get_counter_next()

    while current_point != starting_point:
        merged_convex.append(current_point)
        current_point = current_point.get_counter_next()

    visual = merged_convex
    visual.append(starting_point)
    tmp_scatter_plot = Plot.get_plot_instance()
    tmp_scatter_plot.set_convex_hull(visual)
    tmp_scatter_plot.create_scatter_plot()

    merged_convex.sort(key=lambda p: p.get_x())

    return merged_convex


def find_lower_tan(left_convex, right_convex):
    left_start = len(left_convex) - 1
    right_start = 0
    lower_tangent = Line(left_convex[left_start], right_convex[right_start])

    lower_tangent_found = False

    while not lower_tangent_found:

        left_tan_found = lower_tangent.point_above_line(lower_tangent.get_starting_point().get_clock_next())
        while not left_tan_found:
            lower_tangent.set_starting_point(lower_tangent.get_starting_point().get_clock_next())
            left_tan_found = lower_tangent.point_above_line(lower_tangent.get_starting_point().get_clock_next())

        right_tan_found = lower_tangent.point_above_line(lower_tangent.get_ending_point().get_counter_next())
        while not right_tan_found:
            lower_tangent.set_ending_point(lower_tangent.get_ending_point().get_counter_next())
            right_tan_found = lower_tangent.point_above_line(lower_tangent.get_ending_point().get_counter_next())

        left_tan_found = lower_tangent.point_above_line(lower_tangent.get_starting_point().get_clock_next())
        if left_tan_found and right_tan_found:
            lower_tangent_found = True

    return lower_tangent


def find_upper_tan(left_convex, right_convex):
    left_start_index = len(left_convex) - 1
    right_start_index = 0
    upper_tangent = Line(left_convex[left_start_index], right_convex[right_start_index])

    upper_tangent_found = False

    while not upper_tangent_found:

        left_tan_not_found = upper_tangent.point_above_line(upper_tangent.get_starting_point().get_counter_next())
        while left_tan_not_found:
            upper_tangent.set_starting_point(upper_tangent.get_starting_point().get_counter_next())
            left_tan_not_found = upper_tangent.point_above_line(upper_tangent.get_starting_point().get_counter_next())

        right_tan_not_found = upper_tangent.point_above_line(upper_tangent.get_ending_point().get_clock_next())
        while right_tan_not_found:
            upper_tangent.set_ending_point(upper_tangent.get_ending_point().get_clock_next())
            right_tan_not_found = upper_tangent.point_above_line(upper_tangent.get_ending_point().get_clock_next())

        left_tan_not_found = upper_tangent.point_above_line(upper_tangent.get_starting_point().get_counter_next())
        if not (left_tan_not_found and right_tan_not_found):
            upper_tangent_found = True

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
