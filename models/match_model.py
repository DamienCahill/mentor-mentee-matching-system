from DBcm import UseDatabase
from config import config

def create_match(mentor_id, submission_id, timestamp):
    with UseDatabase(config) as cursor:
        cursor.execute('INSERT INTO matches (time_accepted, mentor_id, submission_id) VALUES (%s, %s, %s)', (timestamp, mentor_id, submission_id))

def get_matches_submission_ids(mentor_id):
    with UseDatabase(config) as cursor:
        sql = f"SELECT submission_id FROM matches WHERE mentor_id={mentor_id}"
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def get_matches(mentor_id):
    with UseDatabase(config) as cursor:
        sql = f"""
            SELECT questionnaire_submission.id,
                open_text_answer.answer, matches.time_accepted
             FROM questionnaire_submission
             inner join open_text_answer on 
             questionnaire_submission.id = open_text_answer.submission_id
             inner join matches on
             matches.submission_id = questionnaire_submission.id
             where open_text_answer.question_id = 1 and 
             matches.mentor_id={mentor_id}
        """
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res