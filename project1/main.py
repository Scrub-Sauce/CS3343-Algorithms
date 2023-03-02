from Plot import Plot
from Point import Point
from Line import Line

if __name__ == "__main__":
    scatter_plot = Plot.get_plot_instance()
    scatter_plot.populate("input.csv")

    print(scatter_plot)
