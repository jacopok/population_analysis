from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


from population_analysis.utils import read_file, select_by_common_envelope

base = Path(__file__).parent / 'data'

def compute_n_by_comenv():

    Zs = []
    n_comenv = []
    n_tot = []

    for Z in np.arange(1, 10_000) / 10_000:
        
        em_file = base / f'Z_{Z:.4f}evol_mergers.out'
        m_file = base / f'Z_{Z:.4f}mergers.out'

        try:
            cols = read_file(em_file)
        except FileNotFoundError:
            continue

        try:
            ce, nce = select_by_common_envelope(cols)
        except ValueError:
            continue

        print(f'Z={Z}')
        print(f'With common envelope: {len(ce)}')
        print(f'Without common envelope: {len(nce)}')
        
        Zs.append(Z)
        n_comenv.append(len(ce))
        n_tot.append(len(ce) + len(nce))

        merg = read_file(m_file)
        if len(merg) != len(ce) + len(nce):
            print('Merger number does not match!')
        print(f'Mergers: {len(ce) + len(nce)}')

        Zs = np.array(Zs)
        n_comenv = np.array(n_comenv)
        n_tot = np.array(n_tot)

        return Zs, n_comenv, n_tot

def merger_efficiency():
    
    total_mass = 4313370.713
    
    try:
        Zs = np.load('Zs.npy')
        n_comenv = np.load('n_comenv.npy')
        n_tot = np.load('n_tot.npy')
    except FileNotFoundError:
        Zs, n_comenv, n_tot = compute_n_by_comenv()
        np.save('Zs', Zs)
        np.save('n_comenv', n_comenv)
        np.save('n_tot', n_tot)
    
    plt.plot(Zs, n_tot / total_mass, c='black', label='All mergers')
    plt.plot(Zs, n_comenv / total_mass, c='black', ls=':', label='Mergers with common envelope')
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Metallicity $Z$')
    plt.ylabel('Mergers per ZAMS mass [$M_{\odot}^{-1}$]')
    plt.legend()

    ax2 = plt.gca().twinx()
    ax2.plot(Zs, n_tot / 200_000, alpha=0)
    ax2.set_ylabel('Mergers per ZAMS binary [dimensionless]')
    ax2.set_yscale('log')
    


if __name__ == "__main__":
    from make_all_figures import plot_and_save
    plot_and_save(merger_efficiency)