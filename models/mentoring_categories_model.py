from DBcm import UseDatabase
config = {
    'host':'db',
    'database':'mentor_mentee_matching_system',
    'user':'root',
    'password':'devpass'
}

def get_all_mentoring_categories():
    with UseDatabase(config) as cursor:
        sql = "SELECT * FROM mentoring_categories"
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def get_mentor_mentoring_categories(mentor_id):
    with UseDatabase(config) as cursor:
        sql = f"""
            SELECT mentoring_categories.id, mentoring_categories.name FROM mentoring_categories 
            inner join mentor_profiles on 
            mentoring_categories.id = mentor_profiles.mentoring_category_id
            WHERE mentor_profiles.mentor_id = {mentor_id}
        """
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def delete_mentor_mentoring_category(mentor_id, mentor_mentoring_category):
    with UseDatabase(config) as cursor:
        sql = "DELETE FROM mentor_profiles where mentor_id = %s and mentoring_category_id= %s"
        cursor.execute(sql, (mentor_id, mentor_mentoring_category))

def add_mentor_mentoring_category(mentor_id, mentor_mentoring_category):
    with UseDatabase(config) as cursor:
        sql = "INSERT INTO mentor_profiles (mentor_id, mentoring_category_id) VALUES (%s, %s)"
        cursor.execute(sql, (mentor_id, mentor_mentoring_category))
