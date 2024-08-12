import random

weight = round(random.uniform(0.10, 50.00), 2)

rate_2_pounds = 1.50
rate_6_pounds = 3.00
rate_10_pounds = 4.00
rate_over_10_pounds = 4.75

if weight <= 2:
    shipping_cost = round(weight * rate_2_pounds, 2)
elif weight <= 6:
    shipping_cost = round(weight * rate_6_pounds, 2)
elif weight <= 10:
    shipping_cost = round(weight * rate_10_pounds, 2)
else:
    shipping_cost = round(weight * rate_over_10_pounds, 2)

print(f"Weight: {weight} pounds")
print(f"Shipping cost: ${shipping_cost}")
