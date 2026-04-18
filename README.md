# Bond Evaluation

## Overview
A Python tool for pricing a 10-year German government bond using real yield curve data. Computes the Net Present Value (NPV) of cash flows by applying annually averaged yields extracted from Nelson-Siegel-Svensson beta scenarios, then compares that against a flat-yield baseline.

## Problem It Solves
- Manual bond pricing with a flat discount rate ignores the shape of the actual yield curve, leading to inaccurate valuations
- Processing raw yield curve CSV data from sources like the ECB into usable per-year discount rates requires non-trivial data wrangling
- Target users: finance students and analysts who want to experiment with yield-curve-based bond pricing in Python

## Use Cases
1. A student prices a 2.6% coupon bond against ECB yield curve data to see how the term structure affects valuation compared to using a single flat yield
2. An analyst swaps in a different `beta_scenarios_*.csv` file to price the same bond under alternative interest rate scenarios (e.g. stress tests)
3. A researcher extends `main.py` to loop over multiple bonds and output a comparison table of NPVs across yield curve scenarios

## Key Features
- **Yield curve integration** — reads Nelson-Siegel-Svensson beta parameters from CSV and averages per maturity year
- **Scenario files** — four pre-built scenarios (`IF`, `PY`, `SR`, baseline) for different rate environments
- **Flat-yield fallback** — if a year's data is missing, the calculation falls back to a hardcoded flat yield
- **Minimal dependencies** — only `pandas` required

## Tech Stack
- Python 3.8+
- pandas

## Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/Isolaee/BondEvaluation.git
cd BondEvaluation

# 2. Install dependencies
pip install pandas

# 3. Run the pricing script
python code/main.py
```

Output prints the per-year average yields and the NPV of the bond under those yields.

### Customising the bond

Edit the parameters at the top of `code/main.py`:

```python
coupon      = 2.6    # annual coupon rate (%)
yield_rate  = 2.71   # fallback flat yield (%)
face_value  = 100    # par value
```

### Switching yield curve scenarios

Change the file loaded in `main.py` to one of the other scenario files:

| File | Description |
|---|---|
| `beta_scenarios_IF.csv` | Instantaneous forward rate scenario |
| `beta_scenarios_PY.csv` | Par yield scenario |
| `beta_scenarios_SR.csv` | Spot rate scenario |
| `beta_scenarios.csv` | Baseline |
