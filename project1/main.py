from Plot import Plot

if __name__ == "__main__":
    scatter_plot = Plot.get_plot_instance()
    scatter_plot.populate("input.csv")
    print(scatter_plot)
    scatter_plot.find_convex_hull()
    scatter_plot.create_scatter_plot()
