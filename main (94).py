import sqlite3

def create_database():
    # Establish a connection to the SQLite database
    conn = sqlite3.connect('cps_database.db')
    c = conn.cursor()

    # Create the Children table
    c.execute('''CREATE TABLE IF NOT EXISTS Children
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  age INTEGER,
                  address TEXT,
                  parent_guardian TEXT,
                  contact TEXT)''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def add_child(child_data):
    # Establish a connection to the SQLite database
    conn = sqlite3.connect('cps_database.db')
    c = conn.cursor()

    # Insert the child data into the Children table
    c.execute("INSERT INTO Children (name, age, address, parent_guardian, contact) VALUES (?, ?, ?, ?, ?)",
              (child_data['name'], child_data['age'], child_data['address'], child_data['parent_guardian'], child_data['contact']))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def search_children_by_town(town):
    # Establish a connection to the SQLite database
    conn = sqlite3.connect('cps_database.db')
    c = conn.cursor()

    # Retrieve child information based on town
    c.execute("SELECT * FROM Children WHERE address LIKE ?", ('%'+town+'%',))
    children = c.fetchall()

    # Print the child information
    for child in children:
        print(f"ID: {child[0]}, Name: {child[1]}, Age: {child[2]}, Address: {child[3]}, Parent/Guardian: {child[4]}, Contact: {child[5]}")

    # Close the connection
    conn.close()

# Create the database and table if they don't exist
create_database()

# Test adding a child record
child_data = {
    'name': 'John Doe',
    'age': 8,
    'address': '123 Elm Street, Anytown, NY',
    'parent_guardian': 'Jane Doe',
    'contact': '555-1234'
}
add_child(child_data)

# Test searching for children in a specific town
search_children_by_town('Anytown')
