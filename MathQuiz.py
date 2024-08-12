import random


def math_quiz():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)

    print(f"   {num1}\n+  {num2}\n------")

    user_answer = int(input("Enter the answer: "))

    correct_answer = num1 + num2
    if user_answer == correct_answer:
        print("You are correct!")
        return True
    else:
        print("Incorrect, the correct answer is", correct_answer)
        return False


total_questions = int(input("How many questions would you like to answer? "))
correct_count = 0

for _ in range(total_questions):
    correct = math_quiz()
    if correct:
        correct_count += 1

percent_right = 100 * (correct_count / total_questions)

print(f"You got {correct_count} out of {total_questions}")
print(f"Your score: {percent_right:.0f}%")
