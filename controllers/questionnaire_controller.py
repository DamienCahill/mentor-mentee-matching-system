from flask import Flask, request, render_template, session,flash, redirect,url_for, Blueprint
from auth.auth import login_required
from auth.authz import admin_role_required
from models.questionnaire_model import (
    get_open_text_questions, 
    get_likert_scale_questions, 
    create_questionnaire_submission, 
    insert_answer,
    get_submissions,
    get_submission,
    get_open_text_answers,
    get_likert_scale_answers
)
import time

questionnaire_controller_bp = Blueprint('questionnaire_controller_bp',__name__)

@questionnaire_controller_bp.route("/questionnaire", methods=["GET"]) 
def view_questionnaire():
    # Get questions from the db
    open_text_questions = get_open_text_questions()
    likert_scale_questions = get_likert_scale_questions()
    # Display the questionnaire
    return render_template("questionnaire.html", open_text_questions = open_text_questions, likert_scale_questions = likert_scale_questions)

@questionnaire_controller_bp.route("/submit-questionnaire", methods=["POST"])
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
    return render_template("thank_you.html")

@questionnaire_controller_bp.route("/questionnaires/submissions", methods=["GET"])
@login_required
@admin_role_required
def view_submitted_questionnaires():
    return render_template("questionnaire_submission/list.html")

@questionnaire_controller_bp.route("/questionnaires/get-all-submissions", methods=["GET"])
@login_required
@admin_role_required
def get_submitted_questionnaires():
    submissions =  get_submissions()
    return submissions

@questionnaire_controller_bp.route('/questionnaires/submission/<submission_id>')
@login_required
def view_submitted_questionnaire(submission_id):
    if int(submission_id) not in session.get('submission_matches', []):
        flash("You do not have permission to view that page. You have been redirected.", 'danger')
        return redirect(url_for('dashboard_controller_bp.load_dashboard'))
    likert_scale_answers = get_likert_scale_answers(submission_id)
    open_text_answers = get_open_text_answers(submission_id)
    return render_template("questionnaire_submission/view_submission.html", open_text_questions = open_text_answers, likert_scale_questions = likert_scale_answers)