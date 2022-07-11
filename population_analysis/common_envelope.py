import pandas as pd
import numpy as np

from .plotting import FILENAMES, EVOL_FILENAMES
from .utils import read_file

def select_by_common_envelope(df_evol: pd.DataFrame, df_merg: pd.DataFrame):
    
    indices_common_envelope: list[int] = []
    
    for _, row in df_evol.iterrows():
        if row['label'] == 'COMENV':
            indices_common_envelope.append(row['#ID'])
    
    # mergers = df[df['label'] == 'COELESCE']
    
    has_comenv = np.vectorize(lambda index: index in indices_common_envelope)
    
    mergers_comenv = df_merg[has_comenv(df_merg['#ID'])]
    mergers_no_comenv = df_merg[np.logical_not(has_comenv(df_merg['#ID']))]
    
    return mergers_comenv, mergers_no_comenv

def split_by_comenv(data, Z: str):
    
    df_evol = read_file(EVOL_FILENAMES[Z])
    return select_by_common_envelope(df_evol, data)