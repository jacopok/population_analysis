import numpy as np
import matplotlib.pyplot as plt

def read_file(filename: str) -> tuple[list[str], np.ndarray]:
    """Read the given file and return
    its headers, as a list of strings, as well as the corresponding
    data as a numpy array.

    Parameters
    ----------
    filename : str

    Returns
    -------
    headers: list[str]
    numeric_data: np.ndarray
        The shape of this array is (n_data, n_parameters).
    """
    
    bad_strings = []
    
    def is_allowed(value: str):
        
        if value in bad_strings:
            return False
        
        try:
            float(value)
            return True
        except ValueError:
            bad_strings.append(value)
            return False

    data = []

    with open(filename, 'r') as f:
        lines = f.readlines()

        header = [val for val in lines[0].split(' ') if val != '']

        data.extend([x for x in line.split(' ') if is_allowed(x)] for line in lines[1:])
    
    numeric_data = np.array(data, dtype=float)
    
    return header, numeric_data
    