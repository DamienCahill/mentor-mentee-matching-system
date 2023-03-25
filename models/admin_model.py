from DBcm import UseDatabase

config = {
    'host':'db',
    'database':'mentor_mentee_matching_system',
    'user':'root',
    'password':'devpass'
}
    
def create_admin(self, email, first_name, last_name, password):
	with UseDatabase(config) as cursor:
        sql = "INSERT INTO users (email, first_name, last_name, password, role) VALUES (%s, %s, %s, %s, 1)"
        cursor.execute(sql, (email, first_name, last_name, password))

def update_admin(self, admin_id, email, first_name, last_name):
    with UseDatabase(config) as cursor:
        sql = "UPDATE users SET email=%s, first_name=%s, last_name=%s WHERE id=%s AND role=1"
        cursor.execute(sql, (email, first_name, last_name admin_id))

def delete_admin(self, admin_id):
    with UseDatabase(config) as cursor:
        sql = "DELETE FROM users WHERE id=%s AND role=1"
        cursor.execute(sql, (admin_id,))

def view_all_admins(self):
    with UseDatabase(config) as cursor:
        sql = "SELECT id, email, first_name, last_name FROM users WHERE role=1"
        cursor.execute(sql)
    return cursor.fetchall()

def view_admin(self, admin_id):
    with UseDatabase(config) as cursor:
        sql = "SELECT id, email, first_name, last_name FROM users WHERE id=%s AND role=1"
        cursor.execute(sql, (admin_id,))
    return cursor.fetchone()
