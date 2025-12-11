# Investigating Price-Fixing in U.S. Ground Beef

**Institution:** University of Toronto, Department of Economics  
**Course:** ECO421: Special Topics in Economics - Competition Policy  
**Instructor:** Nadia Soboleva  
**Grade:** 92%  

## Overview

This research investigates whether long-term U.S. ground beef prices exhibit patterns consistent with price-fixing behaviour, broadly following Clark et al.’s (2024) analytical framework for hub-and-spoke cartels in the North American grocery industry. Aggregate monthly price data and industry-specific CPIs and PPIs from the Federal Reserve Economic Data and Statistics Canada are incorporated into logarithmic difference-in-differences regressions to evaluate suspected collusion periods. Non-implicated protein categories—dried beans, cheddar cheese, whole milk—serve as control groups to isolate anti-competitive effects. Results reveal mixed evidence in favour of the hypothesis and suggest concurrent cartelisation across U.S. and Canadian beef markets.

## Motivation

This project allowed me to move beyond abstract theoretical ruminations about how markets operate by empirically searching for irregularities within commodity markets. Given the tangible social consequences of rising grocery costs for consumers, integrity in market outcomes is not only economically but also morally paramount. Specifying suitable controls was itself an exercise in creativity as virtually every major animal protein alternative—poultry, pork, fish, eggs—had been implicated in collusion, forcing a careful balance between theoretical substitutability and data availability.

## Replication

To instantly run the full analysis, without any local setup: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/suha2502/econometrics-portfolio/blob/main/03-beef-collusion/beef_collusion_analysis.ipynb).

## Repository Structure

```
econometrics-portfolio/
├─ 03-beef-collusion/
│  ├─ data/
│  │  ├─ raw/
│  │  │  └─ data_description.yaml
│  │  └─ derived/ 
│  ├─ results/ 
│  ├─ beef_collusion_analysis.ipynb   ➔ full Python workflow in Jupyter Notebook
│  ├─ beef_collusion_paper.pdf        ➔ write-up
│  ├─ packages.txt
│  └─ README.md
```
