import random

num_numbers = int(input("How many random numbers would you like? (up too 1000) "))
num_numbers = min(num_numbers, 1000)

with open("random_numbers.txt", "w") as file:
    count = 0
    while count < num_numbers:
        numbers = [str(random.randint(1, 500)) for _ in range(min(10, num_numbers - count))]
        line = ",".join(numbers)
        file.write(line)
        count += len(numbers)
        if count < num_numbers:
            file.write("\n")
print("Random numbers have been written to random_numbers.txt")
