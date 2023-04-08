from DBcm import UseDatabase
config = {
    'host':'db',
    'database':'mentor_mentee_matching_system',
    'user':'root',
    'password':'devpass'
}

def get_open_text_questions():
    with UseDatabase(config) as cursor:
        sql = "SELECT * FROM open_text_question"
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def get_likert_scale_questions():
    with UseDatabase(config) as cursor:
        sql = "SELECT * FROM likert_scale_question"
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def create_questionnaire_submission(time_submitted):
    with UseDatabase(config) as cursor:
        cursor.execute('INSERT INTO questionnaire_submission (time_submitted) VALUES (%s)', (time_submitted,))
        submission_id = cursor.lastrowid

    return submission_id

def insert_answer(submission_id, question_id, answer, answer_type):
    with UseDatabase(config) as cursor:
        sql = f'INSERT INTO {answer_type}  VALUES (null, "{question_id}", "{answer}", "{submission_id}")'
        cursor.execute(sql)
