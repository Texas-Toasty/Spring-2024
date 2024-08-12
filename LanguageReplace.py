import os

with open("favorite_language.txt", "r") as input_file, open("temp.txt", "w") as temp_file:
    for line in input_file:
        changed_line = line.replace("Java", "Python")
        temp_file.write(changed_line)

os.replace("temp.txt", "favorite_language.txt")

print("File replacement complete.")
