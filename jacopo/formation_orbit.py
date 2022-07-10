import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy.optimize import fsolve

from population_analysis.plotting import make_vid_varying_metallicity, plot_at_metallicity


def logit(x):
    return np.log(x / (1-x))

def inv_logit(y):
    return 1 / (np.exp(-y) + 1)

def log_g(e):
    return np.log(e ** (12 / 19) / (1 - e ** 2) * (1 + 121 / 304 * e ** 2)**(870 / 2299))

def plot_eccentricity(ecc_array, bins):

    hist, bin_edges = np.histogram(logit(ecc_array), bins=bins)

    plt.bar(
        inv_logit(bin_edges[:-1]), 
        hist, 
        width=np.ediff1d(inv_logit(bin_edges)),
        align='edge',
    )
    plt.yscale('log')
    plt.ylim(1/2, 2000)

    plt.xscale('logit')

    plt.ylabel('Mergers per logit eccentricity bin')

def plot_frame_eccentricity(data):
    bins = np.linspace(logit(1e-4), logit(.9999), num=40)
    plot_eccentricity(data['eccform'], bins)
    plt.xlabel('Formation eccentricity [dimensionless, logit scale]')

def get_merger_eccentricities(data):
    ecc = data['eccform']
    a0 = data['sepform']

    # number is 6 * G * Msun / c**2, in solar radii
    afin = (data['m1form'] + data['m2form']) * 1.27350154e-05
    
    a_ratio = a0 / afin
        
    e_new = []

    for e, ar in zip(ecc.values, a_ratio.values):
        log_g_old = log_g(e)
        
        log_g_new = log_g_old - np.log(ar)
        
        to_optimize = lambda new_logit_e : log_g(inv_logit(new_logit_e)) - log_g_new
        
        root, info, ier, msg = fsolve(to_optimize, logit(e/ar), full_output=True)

        if ier != 1:            
            print(f'{log_g_old=}')
            print(f'{log_g_new=}')
            print(msg)
        
        e_new.append(inv_logit(root[0]))
    
    return np.array(e_new)

def plot_frame_merger_eccentricity(data):
    
    merger_eccentricity = get_merger_eccentricities(data)
    bins = np.linspace(logit(1e-12), logit(1/2), num=40)
    plot_eccentricity(e_new, bins)
    plt.xlabel('Merger eccentricity [dimensionless, logit scale]')

def frame_scatter_eccentricity(data):

    merger_eccentricity = get_merger_eccentricities(data)
    ecc = data['eccform']
    
    plt.scatter(ecc.values, merger_eccentricity, s=.5)
    plt.xscale('logit')
    plt.yscale('logit')
    plt.xlabel('Formation eccentricity [dimensionless, logit scale]')
    plt.ylabel('Merger eccentricity [dimensionless, logit scale]')
    
    plt.xlim(1e-4, .999)
    plt.ylim(1e-11, 1e-5)

def frame_scatter_initial_a(data):

    merger_eccentricity = get_merger_eccentricities(data)
    
    plt.scatter(data['sepform'], merger_eccentricity, s=.5)
    plt.xscale('log')
    plt.yscale('logit')
    
    plt.xlabel('Initial separation [$R_{\odot}$, log scale]')
    plt.ylabel('Merger eccentricity [dimensionless, logit scale]')
    
    
    plt.xlim(.2, 100)
    plt.ylim(1e-11, 1e-5)

def plot_frame_scatter_mass(data):

    merger_eccentricity = get_merger_eccentricities(data)

    
    plt.scatter(data['m1form'] + data['m2form'], merger_eccentricity, s=.5)

    plt.xscale('log')
    plt.yscale('logit')
    plt.xlabel('Total mass [$M_{\odot}$, log scale]')
    plt.ylabel('Merger eccentricity [dimensionless, logit scale]')
    
    plt.xlim(3, 100)
    plt.ylim(1e-11, 1e-5)

def plot_frame_scatter_a_ratio_to_merger(data):

    merger_eccentricity = get_merger_eccentricities(data)
    
    plt.scatter(
        data['sepform'] / (data['m1form'] + data['m2form']) / 1.27350154e-05,
        merger_eccentricity, s=.5)

    plt.xlabel(r'$a_{\text{formation}} / R_{\text{ISCO}}$ [dimensionless, log scale]')
    plt.ylabel('Merger eccentricity [dimensionless, logit scale]')
    
    plt.xscale('log')
    plt.yscale('logit')
    
    plt.xlim(1e3, 1e6)
    plt.ylim(1e-11, 1e-5)

if __name__ == '__main__':
    # make_vid_varying_metallicity(plot_frame_eccentricity, 'eccentricity')
    # make_vid_varying_metallicity(plot_frame_merger_eccentricity, 'merger_eccentricity')
    # make_vid_varying_metallicity(
    #     frame_scatter_eccentricity, 
    #     'merger_eccentricity_scatter',
    # )
    plot_at_metallicity(frame_scatter_eccentricity)
    
    # make_vid_varying_metallicity(
    #     frame_scatter_initial_a,
    #     'merger_eccentricity_vs_a'
    # )
    
    plot_at_metallicity(frame_scatter_initial_a)
    
    # make_vid_varying_metallicity(
    #     plot_frame_scatter_mass,
    #     'merger_eccentricity_vs_mass'
    # )
    # make_vid_varying_metallicity(
    #     plot_frame_scatter_a_ratio_to_merger,
    #     'merger_eccentricity_vs_a_ratio_to_merger'
    # )