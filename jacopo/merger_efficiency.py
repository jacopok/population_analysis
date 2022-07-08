from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from population_analysis.utils import read_file, select_by_common_envelope, select_BBH, select_BNS, select_NSBH

base = Path(__file__).parent / 'data'

def compute_n_by_comenv(selector: callable = select_BBH):

    Zs = []
    n_comenv = []
    n_tot = []

    for Z in np.arange(1, 1_000) / 10_000:
        
        em_file = base / f'Z_{Z:.4f}evol_mergers.out'
        m_file = base / f'Z_{Z:.4f}mergers.out'

        try:
            df_evol = read_file(em_file)
            df_merg = read_file(m_file)
            
        except FileNotFoundError:
            continue

        try:
            ce, nce = select_by_common_envelope(df_evol, df_merg)
            ce = selector(ce)
            nce = selector(nce)
        except ValueError:
            continue

        print(f'Z={Z}')
        print(f'With common envelope: {len(ce)}')
        print(f'Without common envelope: {len(nce)}')
        
        Zs.append(Z)
        n_comenv.append(len(ce))
        n_tot.append(len(ce) + len(nce))

        merg = selector(read_file(m_file))
        if len(merg) != len(ce) + len(nce):
            print('Merger number does not match!')
        print(f'Mergers: {len(ce) + len(nce)}')

    Zs = np.array(Zs)
    n_comenv = np.array(n_comenv)
    n_tot = np.array(n_tot)

    return Zs, n_comenv, n_tot

def merger_efficiency():
    
    total_mass = 4_313_370.713
    
    selectors = {
        'BBH': select_BBH ,
        'BNS': select_BNS ,
        'NSBH': select_NSBH ,
    }
    
    cmap = plt.get_cmap('plasma')
   
    colors = {
        'BBH': cmap(.2),
        'BNS': cmap(.5),
        'NSBH': cmap(.8),
    }
    
    ax2_made = False
    
    fig = plt.figure()
    ax = plt.gca()
    ax2 = ax.twinx()
    for name, selector in selectors.items():
        
        print(name)
        Zs, n_comenv, n_tot = compute_n_by_comenv(selector)

        ax.plot(Zs, n_tot / total_mass, c=colors[name], label=f'All {name}')
        ax.plot(Zs, n_comenv / total_mass, c=colors[name], ls=':', label=f'{name} with common envelope')
    
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_xlabel('Metallicity $Z$')
        ax.set_ylabel('Mergers per ZAMS mass [$M_{\odot}^{-1}$]')

        ax2.set_ylabel('Mergers per ZAMS binary [dimensionless]')
        ax2.set_yscale('log')
        ax2.plot(Zs, n_tot / 200_000, alpha=0)

    ax.legend()

if __name__ == "__main__":
    from make_all_figures import plot_and_save
    plot_and_save(merger_efficiency)