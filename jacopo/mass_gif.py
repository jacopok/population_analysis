import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import imageio

from population_analysis.utils import read_file

from mass_distribution import Zs

DATA_PATH = Path(__file__).parent / 'data'

def plot_frame(data):

    total_masses = data['m1form'] + data['m2form']
    mass_ratios = np.maximum(data['m1form'] / data['m2form'], data['m2form'] / data['m1form'])
    
    var_1, var_2 = total_masses, mass_ratios

    kde = gaussian_kde(np.vstack((var_1, var_2)))
    
    V1 = np.linspace(min(var_1), max(var_1), num=200)
    V2 = np.linspace(min(var_2), max(var_2), num=200)
    
    v1_grid, v2_grid = np.meshgrid(V1, V2)
    
    positions = np.vstack([v1_grid.ravel(), v2_grid.ravel()])
    kde_values = kde(positions)
    
    mass_ratio_mask = v1_grid.ravel() < v2_grid.ravel()
    kde_values[mass_ratio_mask] = 0
    
    plt.contourf(
        v1_grid, 
        v2_grid, 
        kde_values.reshape(v1_grid.shape), 
        levels=100,
        cmap=plt.get_cmap('inferno')
    )
    plt.ylim(1, 2.2)
    plt.xlim(3.9, 146)
    plt.gca().set_facecolor('black')
    plt.xlabel('Total mass [$M_{\odot}$]')
    plt.ylabel('Mass ratio')
    
if __name__ == '__main__':

    repeat_frame_times = 3

    for i, Z in enumerate(Zs):
        data = read_file(DATA_PATH / f'mergers_Z={Z}.out')
        plot_frame(data)
        plt.title(f'Z={float(Z):.1e}, N_mergers={len(data["m1form"])}')
        for j in range(repeat_frame_times):
            plt.savefig(f'frames/{repeat_frame_times*i + j}.png')
        plt.close()
    
    gif_name = 'mass_distribution'
    
    with imageio.get_writer(f'{gif_name}.gif', mode='I') as writer:
        for filename in [f'frames/{i}.png' for i in range(repeat_frame_times*len(Zs))]:
            image = imageio.v3.imread(filename)
            writer.append_data(image)
