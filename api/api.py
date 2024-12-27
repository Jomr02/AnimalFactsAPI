import flask
from db import access_db


def get_animals ():
    access_db.get_facts()

