def main():
    total_months = 0
    total_rainfall = 0.0

    years = int(input("Over how many years was rain measured? "))

    for year in range(1, years + 1):

        for month in range(1, 13):
            rainfall = float(input("Enter inches of rainfall for Year {} Month {}: ".format(year, month)))
            total_rainfall += rainfall
            total_months += 1

    average_rainfall = round(total_rainfall / total_months, 1)

    print("Over", total_months, "months")
    print("There was", round(total_rainfall, 1), "inches of rain")
    print("On average, there was", average_rainfall, "per month")


if __name__ == "__main__":
    main()
