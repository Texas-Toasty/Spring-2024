# Function to calculate cost of hot dog with toppings
def calculate_cost(hot_dog_type, toppings):
    base_prices = {"hot dog": 3.50, "chili dog": 4.50}
    topping_prices = {"cheese": 0.50, "peppers": 0.75, "grilled onions": 1.00}

    # Convert hot dog type to lowercase for case-insensitivity
    hot_dog_type_lower = hot_dog_type.lower()

    # Calculate base cost
    base_cost = base_prices.get(hot_dog_type_lower, 0)

    # Calculate cost of toppings
    topping_cost = sum(topping_prices.get(topping, 0) for topping in toppings)

    # Calculate total cost
    total_cost = base_cost + topping_cost

    return total_cost

# Function to print receipt
def print_receipt(hot_dog_type, toppings, total_cost):
    tax_rate = 0.07
    tax = total_cost * tax_rate
    grand_total = total_cost + tax

    # Print receipt
    print("\nReceipt:")
    print("------------------------------")
    print(f"Hot Dog Type: {hot_dog_type.capitalize()}")
    print("Toppings:" if toppings else "No Toppings")
    for topping in toppings:
        print(f"  - {topping.capitalize()}")
    print("------------------------------")
    print(f"Hot Dog Cost: ${total_cost:.2f}")
    print(f"Tax (7%):     ${tax:.2f}")
    print("------------------------------")
    print(f"Total Cost:   ${grand_total:.2f}")
    print("------------------------------")

# Get user input
hot_dog_type = input("Enter the type of hot dog (Hot Dog or Chili Dog): ")
toppings_input = input("Enter toppings (comma-separated, or leave blank): ").lower()
toppings = [topping.strip() for topping in toppings_input.split(',') if topping.strip()]

# Calculate and print receipt
total_cost = calculate_cost(hot_dog_type, toppings)
print_receipt(hot_dog_type, toppings, total_cost)
