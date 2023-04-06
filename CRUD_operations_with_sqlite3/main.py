import sqlite3

# create connection and cursor objects
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# create student table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        major TEXT
    )
''')

# insert data into student table
cursor.execute('''
    INSERT INTO student (name, age, major)
    VALUES (?, ?, ?)
''', ('Somnath Golui', 20, 'Computer Science'))

# commit the transaction
conn.commit()

# retrieve all students from student table
cursor.execute('SELECT * FROM student')
students = cursor.fetchall()
print(students)

# update student data
cursor.execute('''
    UPDATE student
    SET age = ?, major = ?
    WHERE name = ?
''', (21, 'Software Engineering', 'Somnath Golui'))
conn.commit()

# retrieve updated student data
cursor.execute('SELECT * FROM student WHERE name = ?', ('Somnath Golui',))
john_doe = cursor.fetchone()
print(john_doe)

# delete student from student table
cursor.execute('DELETE FROM student WHERE name = ?', ('Somnath Golui',))
conn.commit()

# retrieve all remaining students from student table
cursor.execute('SELECT * FROM student')
students = cursor.fetchall()
print(students)

# close the connection
conn.close()

