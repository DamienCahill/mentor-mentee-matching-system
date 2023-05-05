from DBcm import UseDatabase

config = {
    'host':'db',
    'database':'mentor_mentee_matching_system',
    'user':'root',
    'password':'devpass'
}
    
def insert_admin(email, first_name, last_name, password):
    with UseDatabase(config) as cursor:
        sql = "INSERT INTO users (email, first_name, last_name, password, role_id) VALUES (%s, %s, %s, %s, 1)"
        cursor.execute(sql, (email, first_name, last_name, password))

def update_admin(admin_id, email, first_name, last_name):
    with UseDatabase(config) as cursor:
        sql = "UPDATE users SET email=%s, first_name=%s, last_name=%s WHERE id=%s AND role_id=1"
        cursor.execute(sql, (email, first_name, last_name, admin_id))

def delete_admin(admin_id):
    with UseDatabase(config) as cursor:
        sql = "DELETE FROM users WHERE id=%s AND role_id=1"
        cursor.execute(sql, (admin_id,))

def view_all_admins():
    with UseDatabase(config) as cursor:
        sql = "SELECT id, email, first_name, last_name FROM users WHERE role_id=1"
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def get_admin(admin_id):
    with UseDatabase(config) as cursor:
        sql = "SELECT id, email, first_name, last_name FROM users WHERE id=%s AND role_id=1"
        cursor.execute(sql, (admin_id,))
        res = cursor.fetchone()
    return res
