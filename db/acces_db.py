import sqlite3

def insert_animal_fact(animal, fact):
    conn = sqlite3.connect('animalfacts.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO animalfacts (animal, fact) VALUES (?, ?)', (animal, fact))
        conn.commit()
        return "Fact succesfully created." + animal + fact
    except sqlite3.IntegrityError:
        return "ERROR: Fact already exists" + animal + fact
    finally:
        conn.close()

def mostrar_usuarios():

    conn = sqlite3.connect('animalfacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM animal')
    animalfacts = cursor.fetchall()
    conn.close()

    for fact in animalfacts:
        print(fact)