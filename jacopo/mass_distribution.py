from population_analysis.utils import read_file
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.cm import ScalarMappable
from scipy.stats import gaussian_kde
from pathlib import Path

DATA_PATH = Path(__file__).parent / 'data'
Zs = ['1e-4', '2e-4', '6e-4', '11e-4', '2e-3', '36e-4', '48e-4', '63e-4', '83e-4', '112e-4', '2e-2']


def plot_mass_contours(mass_1, mass_2, color):
    masses_1, masses_2 = [], []
    for m1, m2 in zip(mass_1, mass_2):
        if m2 > m1:
            m1, m2 = m2, m1
        masses_1.append(m1)
        masses_2.append(m2)
    plot_contours(masses_1, masses_2, color)

def plot_total_mass_ratio_contours(mass_1, mass_2, color):
    total_masses = mass_1 + mass_2
    mass_ratios = np.maximum(mass_1 / mass_2, mass_2 / mass_1)
    
    plot_contours(total_masses, mass_ratios, color)

def plot_contours(var_1, var_2, color):

    kde = gaussian_kde(np.vstack((var_1, var_2)))
    
    V1 = np.linspace(min(var_1), max(var_1), num=200)
    V2 = np.linspace(min(var_2), max(var_2), num=200)
    
    v1_grid, v2_grid = np.meshgrid(V1, V2)
    
    positions = np.vstack([v1_grid.ravel(), v2_grid.ravel()])
    kde_values = kde(positions)
    
    mass_ratio_mask = v1_grid.ravel() < v2_grid.ravel()
    kde_values[mass_ratio_mask] = 0
    
    plt.contour(
        v1_grid, 
        v2_grid, 
        kde_values.reshape(v1_grid.shape), 
        levels=1, 
        colors=['white', color, color],
        linestyles=[':', '-', '-'],
    )

if __name__ == '__main__':
    cmap = plt.get_cmap('inferno')
    
    # eventually:
    # [0.0002    , 0.00035566, 0.00063246, 0.00112468, 0.002     ,
    #  0.00355656, 0.00632456, 0.01124683, 0.02      ]
    float_Zs = [float(Z) for Z in Zs]
    norm = LogNorm(vmin = min(float_Zs), vmax=max(float_Zs)*1.5)

    for Z in Zs:
        data = read_file(DATA_PATH / f'mergers_Z={Z}.out')
        plot_total_mass_ratio_contours(data['m1'], data['m2'], cmap(norm(float(Z))))

    plt.colorbar(ScalarMappable(cmap=cmap, norm=norm), label='Metallicity $Z$')

    plt.ylim(1, 2.2)
    plt.xlabel("Total mass [$M_{\odot}$]")
    plt.ylabel("Mass ratio [1]")
    
    plt.savefig('merger_mass_ratios.pdf')
    plt.close()


    for Z in Zs:
        data = read_file(DATA_PATH / f'mergers_Z={Z}.out')
        plot_mass_contours(data['m1'], data['m2'], cmap(norm(float(Z))))
    
    plt.colorbar(ScalarMappable(cmap=cmap, norm=norm), label='Metallicity $Z$')
        
    plt.xlabel("Primary mass [$M_{\odot}$]")
    plt.ylabel("Secondary mass [$M_{\odot}$]")
    
    plt.savefig('merger_masses.pdf')
    plt.close()