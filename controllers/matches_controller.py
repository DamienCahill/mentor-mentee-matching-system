from flask import Flask, request, render_template, session, flash, redirect, url_for, Blueprint
from auth.auth import login_required
import models.mentor_model as mentor_model
import models.mentoring_categories_model as mentoring_categories_model
import models.questionnaire_model as questionnaire_model
import models.match_model as match_model
import time

matches_controller_bp = Blueprint('matches_controller_bp',__name__)

@matches_controller_bp.route("/matches/proposed/<mentor_id>")
@login_required
def get_proposed_matches(mentor_id):
    if session.get('user_role_id',0) != 1 and session.get('userid') != int(mentor_id):
        return redirect(url_for('dashboard_controller_bp.load_dashboard'))
    return render_template('proposed_matches.html',mentor_id=mentor_id)

@matches_controller_bp.route("/matches/proposed-submissions/<mentor_id>")
@login_required
def get_proposed_submission_matches(mentor_id):
    if session.get('user_role_id',0) != 1 and session.get('userid') != int(mentor_id):
        return []
    mentor_categories = mentoring_categories_model.get_mentor_mentoring_categories(mentor_id)
    matching_submissions = get_matching_submissions(mentor_categories)
    if not matching_submissions:
        return []
    session['submission_matches'] = matching_submissions
    submissions = questionnaire_model.get_submissions_from_list_of_ids(tuple(matching_submissions))
    submissions_with_email = []
    accepted_matches = match_model.get_matches_submission_ids(mentor_id)
    accepted_matches_ids = []
    for match_id in accepted_matches:
        accepted_matches_ids.append(match_id[0])
    for submission in submissions:
        if submission[0] in accepted_matches_ids:
            continue
        email = get_email_from_submission(submission[0])
        submissions_with_email.append(submission + tuple([email]))
    return submissions_with_email if submissions_with_email else []

@matches_controller_bp.route("/matches/create/<mentor_id>/<submission_id>")
@login_required
def create_match(mentor_id, submission_id):
    if session.get('user_role_id',0) != 1 and session.get('userid') != int(mentor_id):
        flash('Insufficent permission to create match. You have been redirected.', 'danger')
        return redirect(url_for('dashboard_controller_bp.load_dashboard'))
    timestamp = int(time.time())
    match_model.create_match(mentor_id, submission_id, timestamp)
    flash('Match Successfully Accepted.', 'success')
    return redirect(url_for('dashboard_controller_bp.load_dashboard'))

@matches_controller_bp.route("/matches/<mentor_id>")
@login_required
def view_accepted_matches(mentor_id):
    return render_template('accepted-matches-list.html', mentor_id = mentor_id)
@matches_controller_bp.route("/matches/accepted/<mentor_id>")
@login_required
def get_accepted_matches(mentor_id):
    if session.get('user_role_id',0) != 1 and session.get('userid') != int(mentor_id):
        return []
    matches = match_model.get_matches(mentor_id)
    matches_with_email = []
    for match in matches:
        email = get_email_from_submission(match[0])
        matches_with_email.append(match + tuple([email]))
    return matches_with_email if matches_with_email else []

def get_email_from_submission(submission_id):
    res =  questionnaire_model.get_email_from_submission(submission_id)
    if res:
        return res[0][1]
    else:
        return ""

def get_matching_submissions(mentor_categories):
    submission_weak_categories = get_submissions_weak_mentoring_categories()
    matches = []
    for category in mentor_categories:
        for submission, weak_category in submission_weak_categories.items():
            for weak_category_id in weak_category.keys():
                if category[0] == int(weak_category_id):
                    matches.append(submission)

    return matches

def get_submissions_weak_mentoring_categories():
    submissions = questionnaire_model.get_submissions()
    submission_answers = []
    submission_category_scores = {}
    for submission in submissions:
        # Get the scores and number of scores from questionnaire submission for each mentoring category
        submission_id = submission[0]
        submission_answers = questionnaire_model.get_likert_scale_answers(submission_id)
        submission_answers_by_category = {}
        for answer in submission_answers:
            key = str(answer[2])
            if key in submission_answers_by_category:
                submission_answers_by_category[key]['score_total'] += answer[3]
                submission_answers_by_category[key]['number_of_scores'] += 1
            else:
                submission_answers_by_category[key] ={}
                submission_answers_by_category[key]['score_total'] = answer[3]
                submission_answers_by_category[key]['number_of_scores'] = 1
        submission_category_scores[submission_id] = submission_answers_by_category
    # Get average score from questionnaire submission for each mentoring category
    averages = {}
    for submission, category_scores in submission_category_scores.items():
        category_averages = {}
        for category, scores in category_scores.items():
            average = scores['score_total'] / scores['number_of_scores']
            if average < 2.6: # exclude categories that the mentee is comfortable with.
                category_averages[category] = scores['score_total'] / scores['number_of_scores']
        averages[submission] = category_averages

    return averages