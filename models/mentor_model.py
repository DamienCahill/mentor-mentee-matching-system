from DBcm import UseDatabase
config = {
    'host':'db',
    'database':'mentor_mentee_matching_system',
    'user':'root',
    'password':'devpass'
}
    
def create_mentor(self, email, first_name, last_name, password):
	with UseDatabase(config) as cursor:
        sql = "INSERT INTO users (email, first_name, last_name, password, role) VALUES (%s, %s, %s, %s, 1)"
        cursor.execute(sql, (email, first_name, last_name, password))

def update_mentor(self, mentor_id, email, first_name, last_name):
    with UseDatabase(config) as cursor:
        sql = "UPDATE users SET email=%s, first_name=%s, last_name=%s WHERE id=%s AND role=1"
        cursor.execute(sql, (email, first_name, last_name, password, mentor_id))

def delete_mentor(self, mentor_id):
    with UseDatabase(config) as cursor:
        sql = "DELETE FROM users WHERE id=%s AND role=1"
        cursor.execute(sql, (mentor_id,))

def view_all_mentors(self):
    with UseDatabase(config) as cursor:
        sql = "SELECT id, email, first_name, last_name FROM users WHERE role=1"
        cursor.execute(sql)
    return cursor.fetchall()

def view_mentor(self, mentor_id):
    with UseDatabase(config) as cursor:
        sql = "SELECT id, email, first_name, last_name FROM users WHERE id=%s AND role=1"
        cursor.execute(sql, (mentor_id,))
    return cursor.fetchone()
