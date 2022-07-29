import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.cm import ScalarMappable
from scipy.stats import gaussian_kde
from pathlib import Path

from population_analysis.utils import read_file, select_BBH
from population_analysis.plotting import cmap, plot_and_save, FILENAMES

# def plot_mass_contours(mass_1, mass_2, color):
#     masses_1, masses_2 = [], []
#     for m1, m2 in zip(mass_1, mass_2):
#         if m2 > m1:
#             m1, m2 = m2, m1
#         masses_1.append(m1)
#         masses_2.append(m2)
#     plot_contours(masses_1, masses_2, color)

# def plot_total_mass_ratio_contours(mass_1, mass_2, color):
#     total_masses = mass_1 + mass_2
#     mass_ratios = np.maximum(mass_1 / mass_2, mass_2 / mass_1)
    
#     plot_contours(total_masses, mass_ratios, color)

# def plot_contours(var_1, var_2, color):

#     kde = gaussian_kde(np.vstack((var_1, var_2)))
    
#     V1 = np.linspace(min(var_1), max(var_1), num=200)
#     V2 = np.linspace(min(var_2), max(var_2), num=200)
    
#     v1_grid, v2_grid = np.meshgrid(V1, V2)
    
#     positions = np.vstack([v1_grid.ravel(), v2_grid.ravel()])
#     kde_values = kde(positions)
    
#     mass_ratio_mask = v1_grid.ravel() < v2_grid.ravel()
#     kde_values[mass_ratio_mask] = 0
    
#     plt.contour(
#         v1_grid, 
#         v2_grid, 
#         kde_values.reshape(v1_grid.shape), 
#         levels=1, 
#         colors=['white', color, color],
#         linestyles=[':', '-', '-'],
#     )

def plot_kde(values, bins, density=True, **kwargs):
    if len(values) < 10:
        return
    
    kde = gaussian_kde(values)
    kdevals = kde(bins)
    if not density:
        kdevals *= len(values)
    plt.plot(bins, kdevals, **kwargs)

    # plt.hist(values, 
    #          bins=bins[::20], 
    #          histtype='step', 
    #          density=True, 
    #          **kwargs
    #     )

def mass_ratios():

    Zs = FILENAMES.keys()
    norm = LogNorm(vmin = min(Zs), vmax=.03)
    
    for Z, fname in FILENAMES.items():
        data = select_BBH(read_file(fname))
        plot_kde(data['m1form']/data['m2form'], 
                 bins = np.linspace(0, 5, num=1000),
                color=cmap(norm(float(Z))), 
                alpha=.5
            )

    plt.colorbar(ScalarMappable(cmap=cmap, norm=norm), label='Metallicity $Z$')

    plt.xlabel("Mass ratio [primary/secondary]")
    plt.axvline(1, c='black', ls=':', lw=1.)
    plt.ylabel("Probability density")
    plt.xlim(0, 4)
    
def total_ZAMS_mass():

    Zs = FILENAMES.keys()
    norm = LogNorm(vmin = min(Zs), vmax=.03)
    
    for Z, fname in FILENAMES.items():
        data = select_BBH(read_file(fname))
        plot_kde(
            data['min1']+data['min2'], 
            bins = np.linspace(0, 200, num=1000),
            density=False,
            color=cmap(norm(float(Z))), 
            alpha=.5,
        #   bins=bins,
        #   histtype='step', 
        #   density=True,
        )
        # plot_total_mass_ratio_contours(data['m1form'], data['m2form'], cmap(norm(float(Z))))

    plt.colorbar(ScalarMappable(cmap=cmap, norm=norm), label='Metallicity $Z$')

    plt.xlabel("Total ZAMS mass [$M_{\odot}$]")
    plt.ylabel("Number density")

def total_BBH_mass():

    Zs = FILENAMES.keys()
    norm = LogNorm(vmin = min(Zs), vmax=.03)
    
    for Z, fname in FILENAMES.items():
        data = select_BBH(read_file(fname))
        plot_kde(
            data['m1form']+data['m2form'], 
            bins = np.linspace(0, 100, num=1000),
            density=False,
            color=cmap(norm(float(Z))), 
            alpha=.5,
        )
        # plot_total_mass_ratio_contours(data['m1form'], data['m2form'], cmap(norm(float(Z))))

    plt.colorbar(ScalarMappable(cmap=cmap, norm=norm), label='Metallicity $Z$')

    plt.xlabel("Total BBH mass [$M_{\odot}$]")
    plt.ylabel("Number density")

def merger_time():

    Zs = FILENAMES.keys()
    norm = LogNorm(vmin = min(Zs), vmax=.03)

    
    for Z, fname in FILENAMES.items():
        data = select_BBH(read_file(fname))
        plot_kde(
            np.log(data['tmerg']), 
            bins = np.linspace(0, 12, num=1000),
            density=True,
            color=cmap(norm(float(Z))), 
            alpha=.5,
            #   bins=bins,
            #   histtype='step', 
            #   density=True,
        )
        # plot_total_mass_ratio_contours(data['m1form'], data['m2form'], cmap(norm(float(Z))))

    plt.colorbar(ScalarMappable(cmap=cmap, norm=norm), label='Metallicity $Z$')

    plt.xlabel("Merger time [Myr]")
    plt.gca().xaxis.set_major_formatter(lambda x, pos: f'${np.exp(x):.0f}$')

    plt.axvline(np.log(14451), c='black', ls=':', lw=1., label='Hubble time')

    plt.legend()
    plt.ylabel("Probability density per e-folding")


if __name__ == '__main__':
    
    # eventually:
    # [0.0002    , 0.00035566, 0.00063246, 0.00112468, 0.002     ,
    #  0.00355656, 0.00632456, 0.01124683, 0.02      ]


    # for Z in Zs:
    #     data = read_file(DATA_PATH / f'mergers_Z={Z}.out')
    #     plot_mass_contours(data['m1'], data['m2'], cmap(norm(float(Z))))
    
    # plt.colorbar(ScalarMappable(cmap=cmap, norm=norm), label='Metallicity $Z$')
        
    # plt.xlabel("Primary mass [$M_{\odot}$]")
    # plt.ylabel("Secondary mass [$M_{\odot}$]")
    
    # plt.savefig('merger_masses.pdf')
    # plt.close()
    # plot_and_save(mass_ratios)
    # plot_and_save(total_ZAMS_mass)
    # plot_and_save(total_BBH_mass)
    plot_and_save(merger_time)