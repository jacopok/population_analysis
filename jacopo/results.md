---
title: "MOBSE Results"
author: Jacopo Tissino
date: July 2022
geometry: "left=3.5cm,right=3.5cm,top=3cm,bottom=3cm"
output: pdf_document
colorlinks: true
linkcolor: blue
---

## Initial setup

We perform several runs of the MOBSE code, 
each for 200 thousand binaries with the following parameters,
matching those of the [reference paper](https://arxiv.org/abs/1806.00001):

- the common envelope parameter is set to $\alpha = 1$;
- the primary masses are chosen from a distribution $f(m_1) \propto m^{-2.3}$;
- the secondary masses are chosen by taking a mass ratio $0.1< q < 1$ 
    from a distribution $f(q) \propto q^{-0.1}$;

- the metallicity is varied from $Z = 0.0001$ up to $Z \approx 2 Z_{\odot}$ in small steps;

Quick check: the primary mass function should be $f(m) \propto m^{-2.3}$ from 5 to 150Msun.
The mean mass should then be 
$$ \langle m \rangle 
= \frac{\int m f(m) \text{d} m}{\int f(m) \text{d} m}
= \frac{\int m^{-1.3} \text{d} m}{\int m^{-2.3} \text{d} m}
= \frac{-1.3}{-0.3} \frac{(150^{-0.3} - 5^{-0.3})}{(150^{-1.3} - 5^{-1.3})} M_{\odot}
\approx 14.025 M_{\odot}
$$

Multiplying this by 200k yields 2805020.22, correct to within $0.2\%$ to the value we get 
summing the masses in the input file, 2810624.5673.

I didn't do the check for the secondaries.
The total initial, ZAMS mass is $4313370.713 M_{\odot}$.

## Merger efficiency

![Merger efficiency](merger_efficiency.pdf)

We recover the same qualitative features as figure 14 in the reference paper.
BNS mergers have a roughly flat rate with varying metallicity, with a 
small dip around $Z \sim 10^{-3}$. 

A feature appearing here which is not present in the reference is a 
__peak in themerger rate for roughly solar metallicity__.
The reference stops at $Z = 0.02$: if it had the same feature, we would probably see it
(or at least the left half of the peak).

BBH mergers have a flat-then-decreasing behaviour, with almost no mergers 
occurring above solar metallicity.

BHNS mergers are something of a middle gound, consistent with the reference.

Almost all mergers, in general, occur with a common envelope having taken place.
For BBHs we find the largest deviation from this, mostly at small metallicity.

The overall __normalization__ we find is roughly __an order of magnitude larger__
than that of the reference: BBHs at low metallicity are at $\sim 10^{-3} M_{\odot}^{-1}$
for us, $\sim 10^{-4} M_{\odot}^{-1}$ there, for BNSs we have the same situation 
and order of magnitude below.

All plots hereafter are snapshots of videos capturing the metallicity evolution.

## Mass distribution

![Mass distribution at merger](frame_scatterplot_Z=0.0001.pdf)

At merger, BBHs seem to mostly be close to equal-mass, 
with the original __secondaries__ typically having become the __more massive object__.

NSs seem to have a __mass cut__ around $1.2M_{\odot}$. 

![Mass evolution](frame_initial_final_Z=0.0001.pdf)

There seem to be peculiar features in the ZAMS-to-CO mass relation! 

For primaries, in the $20$ to $35M_{\odot}$ range, 
there appear relations like $M _{\text{CO}} \propto M^2 _{\text{ZAMS}}$.
These are followed very precisely! 
After that, we instead get $M _{\text{CO}} \propto M_{\text{ZAMS}}$.

It looks like _almost_ a fitting formula...
Secondaries mirror this behaviour, but at lower initial masses.

## Eccentricity distribution

![Merger versus formation eccentricity.](frame_scatter_eccentricity_Z=0.0001.pdf)

We show the distribution of eccentricity for BBHs, both at formation
and at merger. 
The eccentricity at merger is computed by assuming that these objects only 
evolve through GW emission, changing their eccentricity and semimajor axis 
while obeying 
$$ \frac{a}{g(e)} = \text{const,} \qquad \text{where}
\qquad
g(e) = \frac{e^{12/19}}{1-e^2} \left(1 + \frac{121}{304} e^2\right)^{870/2299}\,.
$$

We define "merger" as the moment where the semimajor axis equals the ISCO of the binary, $a = 6G(M_1 + M_2) / c^2$.

There is an interesting population of BBHs with __significantly larger eccentricity__ than the bulk;
examining them shows that these are high-eccentricity initial binaries
that also formed with __unusually small initial radii__.

![Merger eccentricity versus initial separation.](frame_scatter_initial_a_Z=0.0001.pdf)

What are these smaller radii due to?