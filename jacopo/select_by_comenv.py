from pathlib import Path
import numpy as np

from population_analysis.utils import read_file, select_by_common_envelope

base = Path(__file__).parent / 'data'

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
    ce, nce = select_by_common_envelope(cols)

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
    print()

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    Zs = np.array(Zs)
    n_comenv = np.array(n_comenv)
    n_tot = np.array(n_tot)
    
    plt.plot(Zs, 1-n_comenv / n_tot)
    plt.xlabel('Metallicity $Z$')
    plt.ylabel('Fraction of mergers without common envelope')
    plt.savefig('mergers_no_comenv.png')