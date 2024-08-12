def taxes(total_sales):
    state_sales_tax = 0.05
    county_sales_tax = 0.025

    county_tax = total_sales * county_sales_tax
    state_tax = total_sales * state_sales_tax
    total_tax = county_tax + state_tax

    return county_tax, state_tax, total_tax


def main():
    total_sales = float(input("Enter this month's total sales: "))
    county_tax, state_tax, total_tax = taxes(total_sales)

    print("\nSales tax report:")
    print(f"County sales tax: ${county_tax:.2f}")
    print(f"State sales tax: ${state_tax:.2f}")
    print(f"Total sales tax: ${total_tax:.2f}")


main()
