from db import db_init
from db import access_db
from api import api

#db_init.db_init()
access_db.insert_animal_fact("Dog", ("Dog Barks"))
api.get_animals()