from population_analysis.utils import run_mobse_changing_metallicity
from datetime import datetime

metallicities = np.arange(1, 101) / 10_000

print(
    'Running with the following metallicities:'
    f'{metallicities}'
)
print(f'This will take about {len(metallicities)*5} minutes')

for i, metallicity in enumerate(metallicities):
    print(f'Running metallicity Z={metallicity}, {i+1}/{len(metallicities)}')
    print(f'Time is {datetime.now()}')
    run_mobse_changing_metallicity(metallicity)