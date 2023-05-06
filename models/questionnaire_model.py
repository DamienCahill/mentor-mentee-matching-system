from DBcm import UseDatabase
from config import config

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

def get_submissions():
    with UseDatabase(config) as cursor:
        sql = """
            SELECT questionnaire_submission.id, questionnaire_submission.time_submitted,
                open_text_answer.answer
             FROM questionnaire_submission
             inner join open_text_answer on 
             questionnaire_submission.id = open_text_answer.submission_id
             where open_text_answer.question_id = 1
        """
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def get_submission(submission_id):
    with UseDatabase(config) as cursor:
        sql = f"""
            SELECT questionnaire_submission.id, questionnaire_submission.time_submitted,
                open_text_answer.answer
             FROM questionnaire_submission
             inner join open_text_answer on 
             questionnaire_submission.id = open_text_answer.submission_id
             where open_text_answer.question_id = 1 AND
             questionnaire_submission.id = {submission_id}
        """
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def get_likert_scale_answers(submission_id):
    with UseDatabase(config) as cursor:
        sql = f"""
            SELECT likert_scale_question.id, likert_scale_question.text, likert_scale_question.mentoring_category_id, likert_scale_answer.answer
            FROM questionnaire_submission
            inner join likert_scale_answer on 
            questionnaire_submission.id = likert_scale_answer.submission_id
            inner join likert_scale_question on 
            likert_scale_question.id = likert_scale_answer.question_id
            where
            questionnaire_submission.id = {submission_id}
        """
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def get_open_text_answers(submission_id):
    with UseDatabase(config) as cursor:
        sql = f"""
            SELECT open_text_question.id, open_text_question.question, open_text_question.input_type, open_text_answer.answer
            FROM questionnaire_submission
            inner join open_text_answer on 
            questionnaire_submission.id = open_text_answer.submission_id
            inner join open_text_question on 
            open_text_question.id = open_text_answer.question_id
            where
            questionnaire_submission.id = {submission_id}
        """
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def get_submissions_from_list_of_ids(ids):
    with UseDatabase(config) as cursor:
        sql = f"""
            SELECT questionnaire_submission.id, questionnaire_submission.time_submitted,
                open_text_answer.answer
             FROM questionnaire_submission
             inner join open_text_answer on 
             questionnaire_submission.id = open_text_answer.submission_id
             where open_text_answer.question_id = 1 AND
             questionnaire_submission.id in {ids}
        """
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

def get_email_from_submission(submission_id):
    with UseDatabase(config) as cursor:
        sql = f"""
            SELECT questionnaire_submission.id,
                open_text_answer.answer
             FROM questionnaire_submission
             inner join open_text_answer on 
             questionnaire_submission.id = open_text_answer.submission_id
             where open_text_answer.question_id = 2 AND
             questionnaire_submission.id = {submission_id}
        """
        cursor.reset()
        cursor.execute(sql)
        res = cursor.fetchall()
    return res
