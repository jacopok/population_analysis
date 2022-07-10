import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy.stats import gaussian_kde
import imageio
from tqdm import tqdm

from population_analysis.plotting import make_vid_varying_metallicity, colors, plot_at_metallicity
from population_analysis.utils import selectors

def plot_frame_kde_total_mass_ratio(data):

    total_masses = data['m1form'] + data['m2form']
    mass_ratios = np.maximum(data['m1form'] / data['m2form'], data['m2form'] / data['m1form'])
    
    var_1, var_2 = total_masses, mass_ratios

    try:
        kde = gaussian_kde(np.vstack((var_1, var_2)))
    except ValueError:
        return
    
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
    plt.ylim(1, 3)
    plt.xlim(1, 100)
    plt.gca().set_facecolor('black')
    plt.xlabel('Total mass [$M_{\odot}$]')
    plt.ylabel('Mass ratio')

def plot_frame_histograms(data):
    mass_1 = data['m1form']
    mass_2 = data['m2form']
    
    bins = np.linspace(0.3, np.log10(150), num=40)
    
    plt.hist(np.log10(mass_1), bins=bins, alpha=.5, label='Primary mass')
    plt.hist(np.log10(mass_2), bins=bins, alpha=.5, label='Secondary mass')

    plt.yscale('log')
    plt.ylim(1/2, 500)
    def tick_label(x, pos):
        return f'{10**x:.1f}'

    plt.xlabel('Mass [$M_{\odot}$]')
    plt.ylabel('Mergers per logarithmic mass bin')
    plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(tick_label))

    plt.legend()

def frame_scatterplot(data):

    for name, selector in selectors.items():
        sub_data = selector(data)
        mass_1 = sub_data['m1form']
        mass_2 = sub_data['m2form']

        plt.scatter(mass_1, mass_2, s=1, label=name, color=colors[name])
        
        plt.plot([1.2, 1.2], [1.2, 80], lw=.5, ls='--', c='black')
        plt.plot([1.2, 80], [1.2, 1.2], lw=.5, ls='--', c='black')

        plt.yscale('log')
        plt.xscale('log')
        plt.xlim(1, 80)
        plt.ylim(1, 80)
        
        r = np.linspace(1, 80)
        plt.plot(r, r, lw=.5, ls=':', c='black')

        plt.xlabel('Primary mass [$M_{\odot}$]')
        plt.ylabel('Secondary mass [$M_{\odot}$]')
    plt.legend()

def frame_initial_final(data):

    for name, selector in selectors.items():
        sub_data = selector(data)
        
        mass_1_in = sub_data['min1']
        mass_2_in = sub_data['min2']

        mass_1 = sub_data['m1form']
        mass_2 = sub_data['m2form']

        plt.scatter(mass_1_in, mass_1, s=1, label=f'{name} primaries', color=colors[name], marker='^')
        plt.scatter(mass_2_in, mass_2, s=1, label=f'{name} secondaries', color=colors[name], marker='o', alpha=.3)
        
        plt.yscale('log')
        plt.xscale('log')
        plt.xlim(2, 180)
        plt.ylim(1, 80)
        
        r = np.linspace(1, 80)
        plt.plot(r, r, lw=.5, ls=':', c='black')

        plt.xlabel('ZAMS mass [$M_{\odot}$]')
        plt.ylabel('CO mass [$M_{\odot}$]')
    plt.legend()
    plt.grid(which='both')

if __name__ == '__main__':

    # make_vid_varying_metallicity(
    #     plot_frame_histograms, 
    #     'mass_histograms', 
    # )
    # make_vid_varying_metallicity(
    #     plot_frame_scatterplot, 
    #     'mass_scatterplot',
    #     selector = lambda x : x
    # )
    # make_vid_varying_metallicity(
    #     frame_initial_final, 
    #     'mass_initial_final',
    #     selector = lambda x : x
    # )
    
    plot_at_metallicity(frame_initial_final, selector = lambda x : x)
    plot_at_metallicity(frame_scatterplot, selector = lambda x : x)


