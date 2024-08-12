import random


def diceroll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2


total_sum = 0

for _ in range(100):
    roll_sum = diceroll()
    total_sum += roll_sum

average = total_sum / 100

print(f"Average of 100 rolls: {average:.2f}")
