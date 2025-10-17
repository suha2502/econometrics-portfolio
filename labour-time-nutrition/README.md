# Can occupational time pressure explain processed food reliance and perceived health among households?

**Institution:** University of Toronto, Department of Economics  
**Course:** ECO483: Health & Economic Inequality
**Instructor:** Michael Stepner

## Overview

This research investigates how occupational time constraints influence reliance on processed foods and self-rated health in the United States. Household-level data on food behaviour and stress from the 2016 Food Acquisition & Purchase Survey and individual-level data on labour and health from the Medical Expenditure Panel Survey are integrated via regional aggregation to enable cross-correlation and geospatial visualization. A standardized household stress index—constructed from perceived time and cost barriers, food insecurity, and recent financial shocks—serves as a proxy for temporal scarcity. Logistic regression specifications estimate how stress, employment characteristics, and demographic factors shape suboptimal dietary decisions. Time-intensive occupations are modestly associated with lower self-rated health. A 1 standard deviation increase in household stress corresponds to a 1.7 percentage point rise in processed-food dependence, suggesting that occupational time pressure may reduce household time budgets, elevate reliance on convenience foods, and serve as a structural channel by which economic inequality maps into health inequality. Potential endogeneity, occupational self-selection, and the inability to merge datasets at the micro-level temper the interpretation of these results.

## Motivation

Inspired by personal observations of divergent household food habits among working families, I designed an empirical study to investigate whether occupational time demands constrain the ability to prepare fresh meals, nudging households toward processed alternatives. This study allowed me to draw from a segment of labour economics, synthesize my interests in health and inequality, while applying rigorous data-analytic methods to a real-world policy-relevant question. By quantifying the potential role of time pressure in nutritional choices, the research illuminates a mechanism through which structural economic factors may translate into disparities in nutrition and health, offering insight into how policy, workplace design, or household-level interventions could alleviate the hidden health costs of contemporary labor demands.

## Final Repository Structure

```
econometrics-portfolio/
├─ labour-time-nutrition/
│  ├─ data/
│  │  ├─ data_description.md
│  │  ├─ raw/ 
│  │  └─ derived/ 
│  ├─ results/ 
│  ├─ labour_time_nutrition_analysis.ipynb   ➔ full Python workflow embedded within a structured Jupyter Notebook
│  ├─ labour_time_nutrition_paper.pdf        ➔ formal write-up
│  ├─ packages.txt
│  ├─ .gitignore
│  └─ README.md
```
```
│  ├─ automation/
│  │  ├─ validate_source_documentation.py
│  │  ├─ upload_data.py
│  │  ├─ submission_validate.py
│  │  ├─ submission_find.py
│  │  ├─ stata_install.py
│  │  ├─ requirements.txt
│  │  ├─ requirements-webupload.txt
│  │  ├─ r_install_dependencies.sh
│  │  ├─ gunicorn_config.py
│  │  ├─ default_commit_message.txt
│  │  └─ config.yaml
│  ├─ README.md
│  ├─ data/ 
│  │  ├─ raw/
│  │  │  ├─ source.yaml
│  │  │  ├─ meps_ipums_extract.csv.dvc
│  │  │  ├─ meps_ipums_codebook.txt.dvc
│  │  │  ├─ faps_individual_puf.csv.dvc
│  │  │  ├─ faps_household_puf.csv.dvc
│  │  │  ├─ faps_fahnutrients.csv.dvc
│  │  │  ├─ cb_2018_us_region_500k.shx.dvc
│  │  │  ├─ cb_2018_us_region_500k.shp.iso.xml.dvc
│  │  │  ├─ cb_2018_us_region_500k.shp.ea.iso.xml.dvc
│  │  │  ├─ cb_2018_us_region_500k.shp.dvc
│  │  │  ├─ cb_2018_us_region_500k.prj.dvc
│  │  │  ├─ cb_2018_us_region_500k.dbf.dvc
│  │  │  ├─ cb_2018_us_region_500k.cpg.dvc
│  ├─ packages.txt
│  ├─ results/ 
│  ├─ labour_time_nutrition_analysis.ipynb   ➔ full Python workflow embedded within a structured Jupyter Notebook
│  ├─ labour_time_nutrition_paper.pdf        ➔ formal write-up
```

## Replication

To run the full analysis instantly, without any local setup: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/suha2502/econometrics-portfolio/blob/main/labour-time-nutrition/labour_time_nutrition_analysis.ipynb).

## Citation

> Kazmi, S. (2025). *The Environmental Impact of a Denim Tax.* University of Toronto, Department of Economics.
> (https://github.com/suha2502/econometrics-portfolio/blob/main/climate-mitigation-policy/denim_tax_paper.pdf)

```
@misc{kazmi2025,
  author = {Kazmi, Suha},
  title = {The Environmental Impact of a Denim Tax},
  year = {2025},
  institution = {University of Toronto, Department of Economics},
  url = {https://github.com/suha2502/econometrics-portfolio/blob/main/climate-mitigation-policy/denim_tax_paper.pdf}}
```

## Contact
I would be honoured to receive any feedback, critiques, or questions! Please feel free to reach out. :)  
**Email:** [suha.kazmi@icloud.com](mailto:suha.kazmi@icloud.com)
**LinkedIn:** [linkedin.com/in/suhakazmi](https://linkedin.com/in/suhakazmi)
