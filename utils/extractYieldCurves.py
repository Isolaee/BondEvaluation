import pandas as pd
import re

# Read the CSV
csv_path = "data/EuroYieldRatesLatest.csv"
df = pd.read_csv(csv_path)

# Extract betas
betas = {}
for beta in ["BETA0", "BETA1", "BETA2", "BETA3"]:
    value = df.loc[df["DATA_TYPE_FM"] == beta, "OBS_VALUE"]
    betas[beta] = float(value.values[0]) if not value.empty else None

# Filter rows for time series (exclude betas)
time_rows = df[~df["DATA_TYPE_FM"].str.contains("BETA")]


def time_to_years_months(time_str):
    match = re.match(r"IF_((\d+)Y)?((\d+)M)?", time_str)
    years = int(match.group(2)) if match and match.group(2) else 0
    months = int(match.group(4)) if match and match.group(4) else 0
    return years, months


time_rows = time_rows.copy()
time_rows[["years", "months"]] = time_rows["DATA_TYPE_FM"].apply(
    lambda x: pd.Series(time_to_years_months(x))
)

# Build scenario columns
for i in range(4):
    beta_name = f"BETA{i}"
    time_rows[beta_name] = time_rows["OBS_VALUE"] * betas[beta_name]

# Final DataFrame
result = time_rows[["years", "months", "BETA0", "BETA1", "BETA2", "BETA3"]]
result = result.sort_values(["years", "months"])
print(result.head())

# Split by prefix in DATA_TYPE_FM and save to separate files
for prefix in ["IF", "SR", "PY"]:
    subset = time_rows[time_rows["DATA_TYPE_FM"].str.startswith(prefix)]
    result_subset = subset[
        ["years", "months", "BETA0", "BETA1", "BETA2", "BETA3"]
    ].sort_values(["years", "months"])
    result_subset.to_csv(f"data/beta_scenarios_{prefix}.csv", index=False)
