import sqlite3
import os


def db_init():
    # Create DB

    db_name = 'animalfacts.db'

    if os.path.exists(db_name):
        os.remove(db_name)

    conn = sqlite3.connect(db_name)

    # Create cursor over DB
    cursor = conn.cursor()

    # Create the table
    cursor.execute("CREATE TABLE IF NOT EXISTS animalfacts (animal VARCHAR(50) NOT NULL,fact VARCHAR(50) NOT NULL, PRIMARY KEY (animal, fact))")

    # Save changes
    conn.commit()
    conn.close()

    print("DB created succesfully")
