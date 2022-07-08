from population_analysis.plotting import plot_and_save

if __name__ == "__main__":

    from select_by_comenv import merger_efficiency

    plotter_list = [
        merger_efficiency
    ]
    for plotting_func in tqdm(plotter_list):
        plot_and_save(plotting_func)