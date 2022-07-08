import subprocess
import os
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from .input_manipulation import read_popsyn, write_popsyn, change_metallicity

MOBSE_PATH = Path(__file__).parent.parent.parent / 'mobse_open'

def read_file(filename: str) -> pd.DataFrame:
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
    
    df = pd.DataFrame.from_dict(return_dict)
    
    # select BBH
    return df[(df['k1form'] == 14) & (df['k2form'] == 14)]

def select_by_common_envelope(df: pd.DataFrame):
    
    indices_common_envelope: list[int] = []
    
    for _, row in df.iterrows():
        if row['label'] == 'COMENV':
            indices_common_envelope.append(row['#ID'])
    
    mergers = df[df['label'] == 'COELESCE']
    
    has_comenv = np.vectorize(lambda index: index in indices_common_envelope)
    
    mergers_comenv = mergers[has_comenv(mergers['#ID'])]
    mergers_no_comenv = mergers[np.logical_not(has_comenv(mergers['#ID']))]
    
    return mergers_comenv, mergers_no_comenv

def run_mobse_changing_metallicity(
    metallicity: float, 
    mobse_path: Path = MOBSE_PATH, 
    out_files: tuple[str] = ('evol_mergers.out', 'mergers.out')):
    """This function will switch to the mobse path, run mobse, 
    and then copy over the files specified as out_files
    (by default evol_mergers.out and mergers.out)
    to the current folder, prepending an indication of the metallicity used.
    """
    
    this_dir = os.getcwd()
    
    for out_file in out_files:
        fname = f'{this_dir}/Z_{metallicity:.04f}{out_file}'
        if os.path.exists(fname):
            print(f'Metallicity {metallicity} already computed')
            return None
    
    os.chdir(mobse_path / 'input')
    rows = read_popsyn('popsyn.in')
    change_metallicity(rows, metallicity)
    write_popsyn(rows, 'popsyn.in')
    
    os.chdir(mobse_path)
    
    subprocess.run(['bash', 'popsyn_runs.sh'])
    
    for out_file in out_files:
        subprocess.run([
            'cp', 
            f'output/A1.0/0.002/{out_file}',  
            f'{this_dir}/Z_{metallicity:.04f}{out_file}'
        ])
    
    os.chdir(this_dir)