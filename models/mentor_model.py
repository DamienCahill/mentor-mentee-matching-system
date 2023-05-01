from DBcm import UseDatabase
config = {
    'host':'db',
    'database':'mentor_mentee_matching_system',
    'user':'root',
    'password':'devpass'
}
    
def insert_mentor(email, first_name, last_name, password):
    with UseDatabase(config) as cursor:
        sql = "INSERT INTO users (email, first_name, last_name, password, role) VALUES (%s, %s, %s, %s, 1)"
        cursor.execute(sql, (email, first_name, last_name, password))

def update_mentor(mentor_id, email, first_name, last_name):
    with UseDatabase(config) as cursor:
        sql = "UPDATE users SET email=%s, first_name=%s, last_name=%s WHERE id=%s AND role=1"
        cursor.execute(sql, (email, first_name, last_name, password, mentor_id))

def delete_mentor(mentor_id):
    with UseDatabase(config) as cursor:
        sql = "DELETE FROM users WHERE id=%s AND role=1"
        cursor.execute(sql, (mentor_id,))

def view_all_mentors():
    with UseDatabase(config) as cursor:
        sql = "SELECT id, email, first_name, last_name FROM users WHERE role_id=2"
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def get_mentor(mentor_id):
    with UseDatabase(config) as cursor:
        sql = "SELECT id, email, first_name, last_name FROM users WHERE id=%s AND role_id=2"
        cursor.execute(sql, (mentor_id,))
        res = cursor.fetchone()
    return res
