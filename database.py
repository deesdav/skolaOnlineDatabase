import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='skolaonline'
)

if mysql.connector:
    print("Database connected")

# Create a cursor object to interact with the database
cursor = cnx.cursor()

try:
    # Execute a query to insert a class record
    cursor.execute("INSERT INTO class (ID, class_name) VALUES ('NULL', '3.Ai')")

    # Commit the changes to the database
    cnx.commit()

    # Inserting a new student record that references the class
    cursor.execute("INSERT INTO student (ID, first_name, last_name, birth_date, class_id) VALUES ('NULL', 'Pavel', 'Pavlos', '2000-01-01', '1')")

    # Commit the changes to the database
    cnx.commit()

    # Execute a query to fetch all class data
    cursor.execute("SELECT * FROM class")

    # Fetch all the data from the executed query
    result = cursor.fetchall()

    # Process the result
    for row in result:
        print(row)

    # Execute a query to fetch all student data
    cursor.execute("SELECT * FROM student")

    # Fetch all the data from the executed query
    result = cursor.fetchall()

    # Process the result
    for row in result:
        print(row)

except mysql.connector.Error as e:
    print("Error:", str(e))

# Close the cursor and the connection
cursor.close()
cnx.close()