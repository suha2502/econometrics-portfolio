# Estimating the Environmental Impact of a Denim Tax

**Institution:** University of Toronto, Department of Economics  
**Course:** ECO481: Special Topics in Economics with Data Analytics – Climate Economics  
**Instructor:** Jeffrey Sun

## Overview

This research considers how a hypothetical Pigouvian tax on Canadian denim jeans would affect their sales, water usage, and carbon emissions. Time-series data on global denim fabric imports from the World Integrated Trade Solution are used to construct jeans-level price and quantity estimates. Published life-cycle environmental cost factors serve as inputs for counterfactual models projecting ecological benefits of internalizing denim's external costs. A first-differenced log-log demand model estimates a short-run own-price elasticity of -1.57. Applying a +20% price shock—calibrated to carbon and water costs—in 2023 predicts a 24% decline in demand from 2022, translating into savings of 0.5 tonnes CO₂-eq emissions and 61 million litres of water. Simplifying assumptions, necessitated by limited public market data and a partial-equilibrium methodology, temper confidence in these first-order approximations. Policy implementation, feasibility, and associated trade-offs are rigorously evaluated.

## Motivation

This was the capstone of a semester-long course where I independently designed an original mitigation policy, from the ground up. It presented a terrific opportunity to meld my deep-rooted interests in fashion and sustainability within an economic framework, exploring policy levers to mollify the tension between denim's cultural allure and its material reality as one of the planet's top resource-intensive textiles. I sought to quantify the effects of corrective pricing in this market and discern whether it could precipitate responsible redirection in an industry emblematic of waste. With the advent of fast fashion and influencer culture, this study offers one take on how policy design might quell socially irresponsible consumption by tethering it directly to personal responsibility.

## Repository Structure

```
econometrics-portfolio/
├─ 01-climate-mitigation-denim/
│  ├─ data/
│  │  ├─ raw/
│  │  │  └─ data_description.md
│  │  └─ derived/
│  ├─ results/
│  ├─ denim_tax_analysis.ipynb   ➔ full Python workflow in Jupyter Notebook
│  ├─ denim_tax_paper.pdf        ➔ formal write-up
│  ├─ packages.txt
│  ├─ .gitignore
│  └─ README.md
```

## Replication

To instantly run the full analysis, without any local setup: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/suha2502/econometrics-portfolio/blob/main/01-climate-mitigation-denim/denim_tax_analysis.ipynb).

## Citation

> Kazmi, S. (2025). *Estimating the Environmental Impact of a Denim Tax.* University of Toronto, Department of Economics.
> (https://github.com/suha2502/econometrics-portfolio/blob/main/01-climate-mitigation-denim/denim_tax_paper.pdf)

```
@misc{kazmi2025,
  author = {Kazmi, Suha},
  title = {Estimating the Environmental Impact of a Denim Tax},
  year = {2025},
  institution = {University of Toronto, Department of Economics},
  url = {https://github.com/suha2502/econometrics-portfolio/blob/main/01-climate-mitigation-denim/denim_tax_paper.pdf}}
```
