### `evol_mergers`

The column names are as follows in `evol_mergers.out`:

```
['#ID', 't_step', 'k1', 'm01', 'mt1', 'logL1', 'logR1', 'logT1', 'mc1',
    'rc1', 'menv1', 'renv1', 'epoch1', 'ospin1', 'dmt1', 'r1/rol1', 'k2',
    'm02', 'mt2', 'logL2', 'logR2', 'logT2', 'mc2', 'rc2', 'menv2', 'renv2',
    'epoch2', 'ospin2', 'dmt2', 'r2/rol2', 'tb', 'sep', 'ecc', 'label',
    'BHspin1', 'BHspin2']
```

Let's explain the relevant ones:

- #ID
- t_step
- k1
- m01
- mt1
- logL1
- logR1
- logT1
- mc1
- rc1
- menv1
- renv1
- epoch1
- ospin1
- dmt1
- r1/rol1
- k2
- m02
- mt2
- logL2
- logR2
- logT2
- mc2
- rc2
- menv2
- renv2
- epoch2
- ospin2
- dmt2
- r2/rol2
- tb
- sep
- ecc
- label: relevant are COELESCE and COMENV
- BHspin1
- BHspin2

### `mergers`

On the other hand, in `mergers.out` we have:

- #ID
- min1: ZAMS mass of primary
- min2: ZAMS mass of secondary
- kick1
- kick2
- cmu1
- cmu2
- tform
- sepform
- eccform
- k1form
- m1form: mass of primary compact object
- k2form
- m2form: mass of secondary compact object
- tmerg
- k1
- m1
- k2
- m2
- sep
- ecc
- label: COELESCE always for mergers
- V1cmX
- V1cmY
- V1cmZ
- V2cmX
- V2cmY
- V2cmZ
- t_SN1
- t_SN2
- BHspin1
- BHspin2

### Questions

For all questions: select events such that `k1form` and `k2form` are both 14, 
since those are BBH mergers.

- Mass function: `m1form`, `m2form` are the masses of the two BHs: 
    - video of mass distributions
- merger efficiency: initial mass function from input file, total rows in `mergers.out`:
    - plot, distinguishing by comenv
- delay times: `tmerg`
- ZAMS masses of progenitors: `min1`, `min2`
- initial $a$ and $e$: `sepform`, `eccform`
- distinguish between comenv and not-comenv: in `mergers_evol`, 
    find a row where `label` is `COMENV` with the same ID

Reading the input file,
the total ZAMS mass is $4313370.713 M_{\odot}$, divided into
2810624.5673 for primaries and
1502746.1457 for secondaries,
for 200k total mergers.

Quick check: the primary mass function should be $m \propto m^{-2.3}$ from 5 to 150Msun.
The mean mass should then be 
$$ \langle m \rangle 
= \frac{\int m f(m) \text{d} m}{\int f(m) \text{d} m}
= \frac{\int m^{-1.3} \text{d} m}{\int m^{-2.3} \text{d} m}
= \frac{-1.3}{-0.3} \frac{(150^{-0.3} - 5^{-0.3})}{(150^{-1.3} - 5^{-1.3})} M_{\odot}
\approx 14.025 M_{\odot}
$$

Multiplying this by 200k yields 2805020.22, correct to within $0.2\%$.
(Also, the error rate is perfectly compatible with $\sqrt{200 000} \approx 450$!)

I didn't do the check for the secondaries.

