import sqlite3

def insert_animal_fact(animal, fact):
    conn = sqlite3.connect('animalfacts.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO animalfacts (animal, fact) VALUES (?, ?)', (animal, fact))
        conn.commit()
        return "Fact succesfully created." + animal + fact
    except sqlite3.IntegrityError:
        return "ERROR: Fact already exists " + animal + ": " + fact
    finally:
        conn.close()

def get_facts(animal = ""):

    conn = sqlite3.connect('animalfacts.db')
    cursor = conn.cursor()
    if animal == "":
        cursor.execute('SELECT * FROM animalfacts')
    else:
        cursor.execute('SELECT * FROM animalfacts WHERE animal =?', (animal,))
        
    animalfacts = cursor.fetchall()
    conn.close()

    fact_dict = {}

    #Get the content of the query into a dictionary
    for fact in animalfacts:
        fact_dict[fact[0]] = fact[1]

    return fact_dict