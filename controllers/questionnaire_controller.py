from __main__ import app
from flask import Flask, request, render_template, session
from auth.auth import login_required
from models.questionnaire_model import (
	get_open_text_questions, 
	get_likert_scale_questions, 
	create_questionnaire_submission, 
	insert_answer,
	get_submissions,
	get_submission
)
import time

@app.route("/questionnaire", methods=["GET"]) 
def view_questionnaire():
	# Get questions from the db
	open_text_questions = get_open_text_questions()
	likert_scale_questions = get_likert_scale_questions()
	# Display the questionnaire
	return render_template("questionnaire.html", open_text_questions = open_text_questions, likert_scale_questions = likert_scale_questions)

@app.route("/submit-questionnaire", methods=["POST"])
def submit_questionnaire():
	# create a submissions in submission table so a submission ID is create
	timestamp = int(time.time())
	submission_id = create_questionnaire_submission(timestamp)
	for key, value in request.form.items():
		split_string = key.split("_")
		answer_type = "_".join(split_string[:-1]).replace("'", "")
		question_id = split_string[-1]
		answer = value
		insert_answer(submission_id, question_id, answer, answer_type)
	return render_template("test.html")

@app.route("/submitted-questionnaires", methods=["GET"]) 
def view_submitted_questionnaires():
	submissions =  get_submissions()
	return render_template("test.html", data=submissions)

@app.route('/submitted-questionnaires/<submission_id>')
def view_submitted_questionnaire(submission_id):
	submissions =  get_submission(submission_id)
	return render_template("test.html", data=submissions)