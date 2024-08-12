budget_amount = float(input("Enter your monthly budget (in $): $"))
total_expenses = 0.0


while True:
    expense_input = input("Enter an expense amount (or 'done' to finish): $")

    if expense_input.lower() == 'done':
        break

    try:
        expense = round(float(expense_input), 2)
        total_expenses += expense
    except ValueError:
        print("Invalid input. Please try again.")

budget_difference = total_expenses - budget_amount

print(f"\nBudgeted amount: ${budget_amount:.2f}")
print(f"Total expenses: ${total_expenses:.2f}")

if budget_difference > 0:
    print(f"You are over by ${budget_difference:.2f}")
if budget_difference < 0:
    print(f"You are under by ${budget_difference:.2f}")
if budget_difference == 0:
    print("You are even $")
