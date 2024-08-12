def kilo_convert(kilometers):
    miles = kilometers * 0.6214
    return round(miles, 2)


try:
    kilometers_input = float(input("Enter distance in kilometers: "))

    miles_result = kilo_convert(kilometers_input)

    print(f"{kilometers_input} kilometers is approximately {miles_result} miles")
except ValueError:
    print("Invalid input. Please try again.")
