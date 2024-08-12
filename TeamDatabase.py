import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Students (studentID INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER,
 gender TEXT, grade TEXT, email TEXT)''')

student_data = [
    (1, 'Ethan', 'Coyour', 20, 'Male', 'Sophomore', 'ethancoyour@gmail.com'),
    (2, 'Jace', 'Moore', 23, 'Male', 'Senior', 'jacemoore3@gmail.com'),
    (3, 'David', 'Schmidt', 22, 'Male', 'Junior', 'davyschmidt@gmail.com'),
    (4, 'Levi', 'Vanderbilt', 22, 'Male', 'Senior', 'levijparry@hotmail.com'),
    (5, 'Jason', 'Hogan', 19, 'Male', 'Freshman', 'jhogan@gmail.com'),
    (6, 'Sophia', 'Johnson', 21, 'Female', 'Sophomore', 'sophjohnson@gmail.com'),
    (7, 'Sam', 'Jones', 20, 'Male', 'Freshman', 'joness13@gmail.com'),
    (8, 'Molly', 'Jacobson', 21, 'Female', 'Junior', 'mollymj18@gmail.com'),
    (9, 'Katelyn', 'Fredrick', 23, 'Female', 'Senior', 'katelynfredrick@gmail.com'),
    (10, 'Peter', 'Perry', 19, 'Male', 'Freshman', 'peterjp@gmail.com')
]

cursor.executemany('INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)', student_data)
conn.commit()
conn.close()
print("Database created")
