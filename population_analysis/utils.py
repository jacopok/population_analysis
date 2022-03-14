import numpy as np
import matplotlib.pyplot as plt

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