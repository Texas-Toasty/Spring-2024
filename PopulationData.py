import sqlite3

conn = sqlite3.connect('population.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE Cities (CityID INTEGER PRIMARY KEY, CityName TEXT, Population INTEGER)''')

cities_data = [
    (1, 'Los Angeles', 2003554),
    (2, 'Boise', 125000),
    (3, 'Minneapolis', 895025),
    (4, 'San Francisco', 1230650),
    (5, 'St. Paul', 649000),
    (6, 'Tallahassee', 590244),
    (7, 'Albuquerque', 240360),
    (8, 'Olympia', 1350670),
    (9, 'Dallas', 990330),
    (10, 'Kansas City', 435997)
]

cursor.executemany('''INSERT INTO Cities (CityID, CityName, Population) VALUES (?, ?, ?)''', cities_data)

conn.commit()
conn.close()
print("Table created")

#  Re-opening the file to print the table in readable text
conn = sqlite3.connect('population.db')
cursor = conn.cursor()

cursor.execute('''SELECT * FROM Cities''')
print("All cities and their populations:")
print(cursor.fetchall())

conn.close()
