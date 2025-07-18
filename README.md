# kg-data-cleaning

This repository contains scripts for cleaning Excel raw data.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place your raw Excel files in `data/raw/`.
3. Run the cleaner specifying the input file (and optionally the output path):
   ```bash
   python src/clean_data.py data/raw/input.xlsx
   ```
   This will produce `data/processed/cleaned.xlsx` by default.

