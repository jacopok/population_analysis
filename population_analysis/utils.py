import subprocess
import os
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from .input_manipulation import read_popsyn, write_popsyn, change_metallicity

MOBSE_PATH = Path(__file__).parent.parent.parent / 'mobse_open'

def read_file(filename: str) -> dict[str, np.ndarray]:
    """Read the given file and return
    its headers, as a list of strings, as well as the corresponding
    data as a numpy array.

    Parameters
    ----------
    filename : str

    Returns
    -------
    data: dict[str, np.ndarray]
        
    """
    
    data = []

    with open(filename, 'r') as f:
        lines = f.readlines()

        header = [val for val in lines[0].split(' ') if val]

        data.extend([x for x in line.split(' ') if x] for line in lines[1:])
    
    
    # only get the name of the column, without the index
    # which is in square brackets
    header = [name.split('[')[0] for name in header]

    return_dict = {}

    for i, name in enumerate(header):
        
        values = [row[i] for row in data]
        try:
            return_dict[name] = np.array(values, dtype=float)
        except ValueError:
            return_dict[name] = np.array(values, dtype=object)
    
    return return_dict

def run_mobse_changing_metallicity(mobse_path: Path = MOBSE_PATH):
    
    this_dir = os.getcwd()
    
    os.chdir(mobse_path / 'input')
    rows = read_popsyn('popsyn.in')
    change_metallicity(rows, .02)
    write_popsyn(rows, 'popsyn.in')
    
    os.chdir(mobse_path)
    
    subprocess.run(['bash', 'popsyn_runs.sh'])
    
    for out_file in ['evol_mergers.out', 'mergers.out']:
        subprocess.run([
            'cp', 
            f'output/A1.0/0.002/{out_file}',  
            f'{this_dir}'
        ])
    
    os.chdir(this_dir)