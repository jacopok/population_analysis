from pathlib import Path

from population_analysis.utils import read_file, select_by_common_envelope

base = Path(__file__).parent / 'data'
em_file = base / 'evol_mergers.out'
m_file = base / 'mergers.out'

cols = read_file(em_file)

ce, nce = select_by_common_envelope(cols)

print(len(ce))
print(len(nce))

merg = read_file(m_file)
print(len(merg))
