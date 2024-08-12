courses_dict = {}

while True:
    course_id = input("Enter Course ID (or type 'done' to finish): ").strip()

    if course_id.lower() == 'done':
        break

    if course_id in courses_dict:
        print("This course ID already exists, please try again.")
        continue

    course_name = input("Enter Course name: ").strip()

    courses_dict[course_id] = course_name

subject = input("Enter a subject: ").strip()

print(f"Courses in {subject}: ")
for course_id, course_name in courses_dict.items():
    if subject.upper() in course_id.upper() or subject.upper() in course_name.upper():
        print(f"{course_id}: {course_name}")
