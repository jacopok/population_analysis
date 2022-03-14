from population_analysis.utils import read_file
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # probably it'd be better to move the files into this folder
    data = read_file('../mobse_open/output/A1.0/0.002/mergers.out')
    plt.hist2d(data['min1'], data['min2'], bins=100)
    plt.show()
