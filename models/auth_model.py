import DBcm
from config import config

def fetch_user_from_credentials(email, password):
    with DBcm.UseDatabase(config) as cursor:
        SQL = """SELECT id FROM users
                 WHERE email=%s AND password=%s"""
        cursor.execute(SQL, (email, password))
        result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return False

def fetch_user_details_as_dictionary_from_id(id):
    with DBcm.UseDatabase(config) as cursor:
        SQL = """SELECT id, email, first_name, last_name, role_id FROM users
                 WHERE id=%s"""
        cursor.execute(SQL, (id,))
        result = cursor.fetchone()
    if result:
        return {
            'user_email' : result[1],
            'user_first_name': result[2],
            'user_last_name' : result[3],
            'user_role_id' : result[4]
        }
    else:
        return False

def update_user_password(user_id, new_password):
    with UseDatabase(dbconfig) as cursor:
        sql = "UPDATE users SET password=%s WHERE id=%s"
        cursor.execute(sql, (new_password, user_id))

