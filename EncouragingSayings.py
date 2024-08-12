import random


def encourage():
    random_number = random.randint(1, 5)

    if random_number == 1:
        print("You got this!")
    elif random_number == 2:
        print("Take one step at a time.")
    elif random_number == 3:
        print("Take a break, breathe, it'll be okay!")
    elif random_number == 4:
        print("Slow down and enjoy life.")
    else:
        print("Even if all seems to be going wrong, God's got you.")


encourage()
encourage()
print("Goodbye")
