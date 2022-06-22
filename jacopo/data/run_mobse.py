import numpy as np
from datetime import datetime

from population_analysis.utils import run_mobse_changing_metallicity

metallicities = np.concatenate((
    np.arange(1, 20, step=1),
    np.arange(20, 50, step=2),
    np.arange(50, 200, step=4),
    np.arange(200, 5000, step=8),
)) / 10_000

print(
    'Running with the following metallicities:'
    f'{metallicities}'
)
print(f'This will take about {len(metallicities)*5} minutes')

for i, metallicity in enumerate(metallicities):
    print(f'Running metallicity Z={metallicity}, {i+1}/{len(metallicities)}')
    print(f'Time is {datetime.now()}')
    run_mobse_changing_metallicity(metallicity)