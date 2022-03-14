from population_analysis.utils import read_file
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from pathlib import Path

DATA_PATH = Path(__file__).parent / 'data'

def plot_contours(mass_1, mass_2, color):
    masses_1, masses_2 = [], []
    for m1, m2 in zip(mass_1, mass_2):
        if m2 > m1:
            m1, m2 = m2, m1
        masses_1.append(m1)
        masses_2.append(m2)

    kde = gaussian_kde(np.vstack((masses_1, masses_2)))
    
    M1 = np.linspace(min(masses_1), max(masses_1), num=200)
    M2 = np.linspace(min(masses_2), max(masses_2), num=200)
    
    m1_grid, m2_grid = np.meshgrid(M1, M2)
    
    positions = np.vstack([m1_grid.ravel(), m2_grid.ravel()])
    kde_values = kde(positions)
    
    mass_ratio_mask = m1_grid.ravel() < m2_grid.ravel()
    kde_values[mass_ratio_mask] = 0
    
    plt.contour(
        m1_grid, 
        m2_grid, 
        kde_values.reshape(m1_grid.shape), 
        levels=2, 
        colors=['white', color, color, color],
        linestyles=[':', '--', '-'],
    )

if __name__ == '__main__':
    cmap = plt.get_cmap('viridis')

    data = read_file(DATA_PATH / 'mergers_Z=2e-4.out')
    plot_contours(data['m1'], data['m2'], cmap(.2))
    

    data = read_file(DATA_PATH / 'mergers_Z=2e-3.out')
    plot_contours(data['m1'], data['m2'], cmap(.5))

    data = read_file(DATA_PATH / 'mergers_Z=2e-2.out')
    plot_contours(data['m1'], data['m2'], cmap(.8))
    
    plt.xlabel("Primary mass [$M_{\odot}$]")
    plt.ylabel("Secondary mass [$M_{\odot}$]")
    
    plt.savefig('merger_masses.pdf')
