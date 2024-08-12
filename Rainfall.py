def data():
    rainfall_data = []
    for month in range(1, 13):
        while True:
            try:
                rainfall = float(input(f"Enter rainfall for month {month}: "))
                if 0.00 <= rainfall <= 99.99:
                    rainfall_data.append(rainfall)
                    break
                else:
                    print("Please enter a valid rainfall amount between 0.00 and 99.99")
            except ValueError:
                print("Invalid input. Please enter a valid number")

    return rainfall_data


def calculate_statistics(rainfall_data):
    total_rainfall = sum(rainfall_data)
    average_rainfall = total_rainfall / len(rainfall_data)
    max_rainfall = max(rainfall_data)
    min_rainfall = min(rainfall_data)
    max_month = rainfall_data.index(max_rainfall) + 1
    min_month = rainfall_data.index(min_rainfall) + 1

    return total_rainfall, average_rainfall, max_month, min_month


def display_statistics(total_rainfall, average_rainfall, max_month, min_month):
    print("\nRainfall Statistics:")
    print(f"Total rainfall for the year: {total_rainfall: .2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Month with the highest rainfall: Month {max_month}")
    print(f"Month with the lowest rainfall: Month {min_month}")


def main():
    print("Enter the rainfall for each month (in inches)")
    rainfall_data = data()
    total_rainfall, average_rainfall, max_month, min_month = calculate_statistics(rainfall_data)
    display_statistics(total_rainfall, average_rainfall, max_month, min_month)


if __name__ == "__main__":
    main()
