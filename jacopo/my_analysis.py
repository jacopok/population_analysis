from population_analysis.utils import read_file
import matplotlib.pyplot as plt

header, data = read_file('../mobse_open/output/A1.0/0.002/mergers.out')

print(header)
plt.hist2d(data[:, 1], data[:, 2], bins=100)
plt.show()
