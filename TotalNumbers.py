try:
    with open("numbers.txt", "r") as file:
        total = 0
        for line in file:
            try:
                number = int(line.strip())
                total += number
            except ValueError:
                print("Error: Invalid value in file.")
except IOError:
    print("Error, unable to read file.")
print("Total is:", total)
