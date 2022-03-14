import numpy as np
import matplotlib.pyplot as plt

def read_file(filename: str):
    
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
    
if __name__ == '__main__':
    # example usage
    # if you have cloned this repo in the same folder as mobse_open

    header, data = read_file('../mobse_open/output/A1.0/0.02/mergers.out')

    print(header)
    plt.hist2d(data[:, 1], data[:, 2], bins=100)
    plt.show()