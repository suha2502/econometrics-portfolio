# Can Occupational Time Pressure Explain Processed Food Reliance and Perceived Health Among Households?

**Institution:** University of Toronto, Department of Economics  
**Course:** ECO483: Health & Economic Inequality
**Instructor:** Michael Stepner
**Grade:** 86%

## Overview

This research evaluates whether occupational time constraints influence reliance on processed foods and self-rated health in the United States. Household-level data from the 2016 Food Acquisition and Purchase Survey and individual-level data from the Medical Expenditure Panel Survey are first analysed separately, then regionally aggregated to enable cross-correlation and geospatial visualization. A standardized household stress index—constructed from perceived time and cost barriers, food insecurity, and recent financial shocks—serves as a proxy for temporal scarcity. Logistic regression specifications estimate how stress, employment characteristics, and demographic factors converge to drive suboptimal dietary decisions. A 1 standard deviation increase in stress corresponds to a 1.7 percentage point increase in processed food dependence, suggesting that occupational time pressure may compress household time budgets, elevate reliance on convenience foods, and thereby operate as a structural channel through which economic inequality maps into health inequality.

## Motivation

Inspired by childhood observations of antithetical food habits among working families, I designed an empirical study to investigate whether occupational time demands constrain households' ability to prepare fresh meals, thereby nudging them towards processed alternatives. This project allowed me to draw on labour and behavioural economics whilst synthesising my interests in health and inequality to answer a policy-relevant question. Quantifying the role of time pressure in nutritional choices may inform workplace-level policy interventions to alleviate the health tolls imposed by contemporary labour demands.

## Repository Structure

```
econometrics-portfolio/
├─ 02-labour-time-nutrition/
│  ├─ data/
│  │  ├─ raw/
│  │  │  └─ data_description.yaml
│  │  └─ derived/ 
│  ├─ results/ 
│  ├─ labour_time_nutrition_analysis.ipynb   ➔ full Python workflow embedded within a structured Jupyter Notebook
│  ├─ labour_time_nutrition_paper.pdf        ➔ formal write-up
│  ├─ packages.txt
│  └─ README.md
```

## Replication

To run the full analysis instantly, without any local setup: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/suha2502/econometrics-portfolio/blob/main/02-labour-time-nutrition/labour_time_nutrition_analysis.ipynb).
