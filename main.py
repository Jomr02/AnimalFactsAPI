from db import db_init
from db import access_db
from api import api

user_input = input("Do you want to reset the Database. Press Y to confirm, press any other key to dismiss")


if user_input == 'Y' or user_input == 'y':
    db_init.db_init()


if __name__ == "__main__":
    api.app.run(debug=True)