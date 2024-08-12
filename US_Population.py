def input_state_data():
    state_data = []
    while True:
        try:
            year_input = input("Enter the year (or 'stop' to end): ")
            if year_input.lower() == 'stop':
                break
            year = int(year_input)
            state = input("Enter the name of the state: ")
            population = int(input("Enter the population: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value for the year.")
            continue

        state_info = [year, state, population]
        state_data.append(state_info)

    return state_data


def calculate_population(state_data, year):
    total_population = 0
    for entry in state_data:
        if entry[0] == year:
            total_population += entry[2]
    return total_population


def main():
    state_data = input_state_data()

    print("\nCollected State Data: ")
    for entry in state_data:
        print(entry)

    while True:
        year_input = input("\nEnter a year to calculate total population (or 'stop' to end): ")
        if year_input.lower() == 'stop':
            break

        try:
            year_input = int(year_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value for the year.")
            continue

        total_population = calculate_population(state_data, year_input)
        print(f"The total population in year {year_input} is {total_population}")

    print("\nProgram Ended")


if __name__ == "__main__":
    main()
