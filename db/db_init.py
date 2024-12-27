import sqlite3


def db_init():
    # Create DB
    conn = sqlite3.connect('animalfacts.db')

    # Create cursor over DB
    cursor = conn.cursor()

    # Create the table
    cursor.execute("CREATE TABLE IF NOT EXISTS animalfacts (animal VARCHAR(50) NOT NULL,fact VARCHAR(50) NOT NULL, PRIMARY KEY (animal, fact))")

    # Save changes
    conn.commit()
    conn.close()

    print("DB created succesfully")
