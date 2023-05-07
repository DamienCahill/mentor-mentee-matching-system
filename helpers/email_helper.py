from DBcm import UseDatabase
from config import config

def email_already_exists(email):
    with UseDatabase(config) as cursor:
        SQL = """SELECT email FROM users
                     WHERE email=%s"""
        cursor.execute(SQL, (email,))
        result = cursor.fetchone()
    return True if result else False
    