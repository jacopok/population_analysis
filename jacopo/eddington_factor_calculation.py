import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as ac
import astropy.units as u

k_e = ac.sigma_T / ac.m_p

from population_analysis.plotting import plot_and_save, cmap

def eddington_factor(luminosity, mass):
    return (k_e / (4 * np.pi * ac.c * ac.G) * luminosity / mass).to(u.dimensionless_unscaled)

# typical MS mass-luminosity relation, L ~ M^3.5
# this is calibrated on local stars though, so we could expect 
# it to be different for lower metallicities
def main_sequence_luminosity(mass, a=3.5):
    return np.minimum(1.4 * ac.L_sun * (mass / u.M_sun)**a, 32600 * ac.L_sun * mass / u.Msun)

def mass_loss_rate(gamma_e, Z = 0.02):
    beta = np.where(
        gamma_e < 2/3,
        0.85,
        np.where(
            gamma_e < 1,
            2.45 - 2.4 * gamma_e,
            0.05
        ))
    return Z**beta

def eddington_factor_plot():

    masses = np.linspace(5, 100, num=400) * u.Msun

    gamma_e = eddington_factor(main_sequence_luminosity(masses), masses)

    fix, axs = plt.subplots(2, 1, sharex=True)

    axs[0].plot(masses, gamma_e, label='Main Sequence stars', c=cmap(.2))
    axs[0].set_ylabel('Eddington factor $\Gamma_e$')
    axs[1].set_xlabel('Mass [$M_{\odot}$]')
    M1 = 47.6
    M2 = 55.5

    axs[0].axhline(2/3, c='black', ls='--', lw=.5)
    axs[0].axvline(M1, c='black', ls='--', lw=.5, label=f'$\Gamma_e = 2/3$, $M = {M1}M_{{\odot}}$')
    axs[0].axvline(M2, c='black', ls=':', lw=.5, label=f'$\Gamma_e = 1$, $M = {M2}M_{{\odot}}$')
    axs[0].legend()

    axs[1].semilogy(masses, mass_loss_rate(gamma_e), c=cmap(.2))
    axs[1].set_ylabel(r'$Z^\beta$')

if __name__ == '__main__':
    plot_and_save(eddington_factor_plot)