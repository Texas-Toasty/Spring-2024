import random


def display_numbers_greater_than(lst, n):
    print(f"Numbers in the list greater than {n}:")
    for num in lst:
        if num > n:
            print(num)


def main():
    random_list = [random.randint(-50, 50) for _ in range(20)]

    random_number = random.randint(-50, 50)

    print(f"Random list: {random_list}")
    print(f"Random number: {random_number}")

    display_numbers_greater_than(random_list, random_number)


if __name__ == "__main__":
    main()
