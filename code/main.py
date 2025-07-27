# Imports

# Bond parameters
coupon = 2.6
yield_rate = 2.71
face_value = 100

# Calculate NPV
npv = (
    sum([coupon / (1 + yield_rate / 100) ** t for t in range(1, 11)])
    + face_value / (1 + yield_rate / 100) ** 10
)
print("NPV:", npv)
