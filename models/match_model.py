from DBcm import UseDatabase
from config import config

def create_match(mentor_id, submission_id, timestamp):
    with UseDatabase(config) as cursor:
        cursor.execute('INSERT INTO matches (time_accepted, mentor_id, submission_id) VALUES (%s, %s, %s)', (timestamp, mentor_id, submission_id))

def get_matches(mentor_id):
    with UseDatabase(config) as cursor:
        sql = f"SELECT submission_id FROM matches WHERE mentor_id={mentor_id}"
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res