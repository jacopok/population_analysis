import numpy as np
import re
from enum import IntEnum

class PopsynColumns(IntEnum):
    bin_id = 0
    zams_m1 = 1
    zams_m2 = 2
    orbital_period = 3
    orbital_eccentricity = 4
    stellar_metallicity = 5
    integration_time = 6

N_COLUMNS = len(PopsynColumns)

def read_popsyn(filename: str):
    
    with open(filename, 'r') as f:
        
        n_mergers = next(f)
        mergers = []
        
        for line in f:
            # remove the newline at the end
            arr = re.split('\s+', line)[:-1]
            assert len(arr) == N_COLUMNS
            mergers.append(arr)

    assert int(n_mergers) == len(mergers)
    
    return np.array(mergers, dtype=str)

def write_popsyn(mergers: np.ndarray, filename: str):

    with open(filename, 'x') as f:
        f.write(f'{len(mergers)}\n')
        for merger in mergers:
            f.write(" ".join(merger) + "\n")

def change_metallicity(mergers: np.array, metallicity: float):
    
    met_string = f'{metallicity:.04f}'
    
    mergers[:, PopsynColumns.stellar_metallicity] = met_string