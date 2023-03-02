from Plot import Plot
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        in_file = "input.csv"
    elif len(sys.argv) == 2:
        in_file = sys.argv[1]
    else:
        sys.stderr.write("Invalid usage: 'python3 main.py' (Assumes input file is named 'input.csv') or 'python3 main.py [filename]'")
        sys.exit(1)

    scatter_plot = Plot.get_plot_instance()
    scatter_plot.populate(in_file)
    scatter_plot.find_convex_hull()
    print(scatter_plot)
    scatter_plot.create_scatter_plot()
