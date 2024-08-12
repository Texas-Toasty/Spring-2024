import sqlite3

conn = sqlite3.connect('textbook.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Book (isbn TEXT PRIMARY KEY, publisher_id TEXT, author_id TEXT, title TEXT,
 print_date TEXT, price REAL)''')

books = [
    {
        'ISBN': '9780451524935',
        'PUBLISHER_ID': 'PUB123',
        'AUTHOR_ID': 'AUTH456',
        'TITLE': '1984',
        'PRINT_DATE': 'July 1, 1950',
        'PRICE': 9.99
    },
    {
        'ISBN': '9780061120084',
        'PUBLISHER_ID': 'PUB456',
        'AUTHOR_ID': 'AUTH789',
        'TITLE': 'To Kill a Mockingbird',
        'PRINT_DATE': 'July 11, 1960',
        'PRICE': 12.99
    },
    {
        'ISBN': '9780061123456',
        'PUBLISHER_ID': 'PUB789',
        'AUTHOR_ID': 'AUTH789',
        'TITLE': 'Go Set a Watchman',
        'PRINT_DATE': 'July 14, 2015',
        'PRICE': 14.99
    },
    {
        'ISBN': '9780062315007',
        'PUBLISHER_ID': 'PUB789',
        'AUTHOR_ID': 'AUTH123',
        'TITLE': 'The Great Gatsby',
        'PRINT_DATE': 'April 10, 1925',
        'PRICE': 11.99
    }
]
books_tuples = [tuple(book.values()) for book in books]

cursor.execute('''CREATE TABLE Publisher (publisher_id TEXT PRIMARY KEY, pub_name TEXT, pub_city TEXT, pub_state TEXT,
 pub_zip TEXT)''')

publishers = [
    {
        'PUBLISHER_ID': 'PUB123',
        'PUB_NAME': 'Penguin Books',
        'PUB_CITY': 'New York',
        'PUB_STATE': 'NY',
        'PUB_ZIP': '10019'
    },
    {
        'PUBLISHER_ID': 'PUB456',
        'PUB_NAME': 'HarperCollins Publishers',
        'PUB_CITY': 'San Francisco',
        'PUB_STATE': 'CA',
        'PUB_ZIP': '94107'
    },
    {
        'PUBLISHER_ID': 'PUB789',
        'PUB_NAME': 'Simon & Schuster',
        'PUB_CITY': 'Los Angeles',
        'PUB_STATE': 'CA',
        'PUB_ZIP': '90064'
    }
]
publishers_tuples = [tuple(publisher.values()) for publisher in publishers]

cursor.execute('''CREATE TABLE Author (author_id TEXT PRIMARY KEY, first_name TEXT, last_name TEXT, author_address TEXT,
 author_city TEXT, author_state TEXT, author_zip TEXT)''')

authors = [
    {
        'AUTHOR_ID': 'AUTH123',
        'FIRST_NAME': 'F. Scott',
        'LAST_NAME': 'Fitzgerald',
        'AUTHOR_ADDRESS': '123 West Egg Street',
        'AUTHOR_CITY': 'West Egg',
        'AUTHOR_STATE': 'NY',
        'AUTHOR_ZIP': '12345'
    },
    {
        'AUTHOR_ID': 'AUTH456',
        'FIRST_NAME': 'George',
        'LAST_NAME': 'Orwell',
        'AUTHOR_ADDRESS': '456 Oceania Boulevard',
        'AUTHOR_CITY': 'London',
        'AUTHOR_STATE': '',
        'AUTHOR_ZIP': '54321'
    },
    {
        'AUTHOR_ID': 'AUTH789',
        'FIRST_NAME': 'Harper',
        'LAST_NAME': 'Lee',
        'AUTHOR_ADDRESS': '789 Finch Lane',
        'AUTHOR_CITY': 'Maycomb',
        'AUTHOR_STATE': 'AL',
        'AUTHOR_ZIP': '67890'
    }
]
authors_tuples = [tuple(author.values()) for author in authors]


print("Tables created")

cursor.executemany('''INSERT INTO Book (isbn, publisher_id, author_id, title, print_date, price) VALUES (?, ?, ?, ?, ?,
 ?)''', books_tuples)
cursor.executemany('''INSERT INTO Publisher (publisher_id, pub_name, pub_city, pub_state, pub_zip) VALUES (?, ?, ?, ?,
 ?)''', publishers_tuples)
cursor.executemany('''INSERT INTO Author (author_id, first_name, last_name, author_address, author_city, author_state,
 author_zip) VALUES (?, ?, ?, ?, ?, ?, ?)''', authors_tuples)

conn.commit()

cursor.execute('''SELECT * FROM book''')
print("Book Table:")
print(cursor.fetchall())

cursor.execute('''SELECT * FROM publisher''')
print("\nPublisher Table:")
print(cursor.fetchall())

cursor.execute('''SELECT * FROM author''')
print("\nAuthor Table:")
print(cursor.fetchall())

conn.close()
