# Does the Attainment of Higher Education Mitigate Racial Disparities in the Uptake of Mental Health Treatment Among Young Adults?

**Institution:** University of Toronto, Department of Economics  
**Course:** ECO483: Health & Economic Inequality  
**Instructor:** Michael Stepner  
**Grade:** 92%

## Overview

This research examines whether higher educational attainment narrows racial gaps in counselling uptake among young adults in the United States. Individual-level data from the National Survey on Drug Use and Health are used to estimate the independent and interactive effects of education and race on the likelihood of engaging in psychotherapy. Logistic regression models yield interpretable marginal effects that contextualize how socioeconomic and racial factors intersect to determine access to care, with results supporting the initial hypothesis.

## Motivation

This project began with a practical question inspired by firsthand experience navigating university health insurance: could direct billing improve young adults' uptake of mental health care? I observed many peers struggle to pursue or stay consistent with therapy, not for lack of trying but because most providers demanded up-front payments for which insurance reimbursements could take weeks to process. For students facing short-term liquidity constraints, such lags rendered continued treatment financially infeasible. While a lack of data precluded testing that particular hypothesis, my intrigue for barriers to access grew. I pivoted to explore whether education might act as an equaliser by facilitating knowledge spillovers across racial strata, offering a physical venue where individuals with greater mental health awareness could diffuse information about its value and available resources to less-informed peers. Conceiving of education as a social mechanism to mitigate disparities in health behaviours deepened my understanding of how privilege and knowledge interact to shape one's propensity to seek help. It also led me to theorise how policy interventions might eradicate the trade-off between meeting immediate financial obligations and investing in one's health—two forms of capital that, at least under current insurance and care structures, remain inextricably linked.

## Replication

To instantly run the full analysis, without any local setup: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/suha2502/econometrics-portfolio/blob/main/04-education-race-therapy/education_race_therapy_analysis.ipynb).

## Repository Structure

```
econometrics-portfolio/
├─ 04-education-race-therapy/
│  ├─ data/
│  │  ├─ raw/
│  │  │  └─ data_description.yaml
│  │  └─ derived/ 
│  ├─ results/ 
│  ├─ education_race_therapy_analysis.ipynb   ➔ full Python workflow in Jupyter Notebook
│  ├─ education_race_therapy_paper.pdf        ➔ write-up
│  ├─ packages.txt
│  └─ README.md
```
