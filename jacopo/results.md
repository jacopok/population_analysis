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
for 200 thousand binaries with the following parameters,
matching those of the [reference paper](https://arxiv.org/abs/1806.00001):

- the common envelope parameter is set to $\alpha = 1$;
- the primary masses are chosen from a distribution $f(m_1) \propto m^{-2.3}$;
- the secondary masses are chose by taking a mass ratio $0.1< q < 1$ 
    from a distribution $f(q) \propto q^{-0.1}$;

- the metallicity is varied from $Z = 0.0001$ up to $Z \approx 2 Z_{\odot}$ in small steps;

## Merger efficiency

![Merger efficiency](merger_efficiency.pdf)

We recover the same qualitative features as figure 14 in the reference paper.
BNS mergers have a roughly flat rate with varying metallicity, with a 
small dip around $Z \sim 10^{-3}$. 

A feature appearing here which is not present in the reference is a 
__peak in themerger rate for roughly solar metallicity__.
The reference stops at $Z = 0.02$: if it had the same feature, we would probably see it.

BBH mergers have a flat-then-decreasing behaviour, with almost no mergers 
occurring above solar metallicity.

BHNS mergers are something of a middle gound, consistent with the reference.

Almost all mergers, in general, occur with a common envelope having taken place.
For BBHs we find the largest deviation from this, mostly at small metallicity.

The overall __normalization__ we find is roughly __an order of magnitude larger__
than that of the reference: BBHs at low metallicity are at $\sim 10^{-3} M_{\odot}^{-1}$
for us, $\sim 10^{-4} M_{\odot}^{-1}$ there, for BNSs we have the same situation 
and order of magnitude below.

