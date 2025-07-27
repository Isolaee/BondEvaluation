# Imports
import pandas as pd

# Bond parameters
coupon = 2.6
yield_rate = 2.71
face_value = 100

# Read beta_scenarios_IF.csv
beta_df = pd.read_csv("data/beta_scenarios_IF.csv")

# Calculate average yield per year for 10 years
avg_yields = []
for year in range(1, 11):
    year_data = beta_df[beta_df["years"] == year]
    avg_yield = year_data["BETA0"].mean() if not year_data.empty else None
    avg_yields.append(avg_yield)

print("10 years average yields (BETA0):", avg_yields)

# Calculate NPV using average yield for each year
npv = (
    sum(
        [
            coupon
            / (
                1
                + (avg_yields[t - 1] if avg_yields[t - 1] is not None else yield_rate)
                / 100
            )
            ** t
            for t in range(1, 11)
        ]
    )
    + face_value
    / (1 + (avg_yields[9] if avg_yields[9] is not None else yield_rate) / 100) ** 10
)
print("NPV (using avg yields):", npv)
