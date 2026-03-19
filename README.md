# Designing European Hydrogen Markets: Perspectives from Transmission System Operators

This repository contains the data, scripts, and supplementary material for the paper:

> **Designing European Hydrogen Markets: Perspectives from Transmission System Operators**
> Marco Saretta, Enrica Raheli, Jalal Kazempour - 

## Overview

The paper investigates the transferability of EU natural gas market mechanisms to emerging hydrogen networks, based on a structured survey of seven European gas Transmission System Operators (TSOs) across six countries. It assesses how established frameworks (covering market and regulatory design, capacity allocation, tariffs, and balancing) may be maintained, adapted, or fundamentally redesigned for hydrogen.

## Repository structure
```
├── data/
│       capacity.csv              # Capacity-related survey data
│       data.csv                  # Main processed dataset
│       pipeline_project.csv      # European hydrogen pipeline project data
│
├── figures/                      # All figures presented in the paper (PDF)
│
├── scripts/
│       api_pipelines.py          # Fetches pipeline project data via API
│       plot_capacity.py          # Generates capacity-related figures
│       plot_SBS.py               # Generates the side-by-side comparison plot
│       plt_ttf_prices.py         # Generates the TTF price figure
│
├── supplementary_material/
│       supplementary_material_hydrogen_market.pdf
│
└── survey/
        EU_Gas_TSO_Hydrogen_questionnaire.pdf   # Survey instrument distributed to TSOs
```

## Reproducing the figures

The scripts require Python and dependencies are managed with [uv](https://github.com/astral-sh/uv). To set up the environment:
```bash
# Install uv if not already available
pip install uv

# Install project dependencies from pyproject.toml
uv sync
```

Then run any script individually, for example:
```bash
uv run scripts/plot_capacity.py
uv run scripts/plt_ttf_prices.py
```

Output figures are written to the `figures/` folder.

## Data and anonymity

Survey responses are attributed at the country level only. Individual TSO and respondent identities are not disclosed, in line with the anonymity guarantees provided to participants at the time of data collection.

## Citation

If you use this repository, please cite:

> Saretta, M., Raheli, E., Kazempour, J. (2025). *Designing European Hydrogen Markets: Perspectives from Transmission System Operators*. Submitted to Energy Policy. DOI: [to be added upon publication]

## License

[To be defined]