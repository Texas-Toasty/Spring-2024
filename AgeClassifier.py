Age = int(input("Enter your age: "))
if Age <= 1:
    print("Infant")
elif 1 < Age < 13:
    print("Child")
elif 13 <= Age < 20:
    print("Teen")
elif Age >= 20:
    print("Adult")
