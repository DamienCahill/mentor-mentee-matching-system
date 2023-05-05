from __main__ import app
from flask import Flask, request, render_template, session, redirect, url_for
import models.mentor_model as mentor_model
import models.mentoring_categories_model as mentoring_categories_model
from helpers.password_helper import generate_random_password, hash_password_string
import sys
from auth.auth import login_required
from auth.authz import admin_role_required

@app.route("/mentors/create", methods=["GET", "POST"])
@login_required
@admin_role_required
def create_mentor():
    if request.method == "GET":
        return render_template('mentor/create.html')
    else:
        # process form
        password = generate_random_password()
        hashed_password = hash_password_string(password)
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        mentor_model.insert_mentor(email,first_name, last_name, hashed_password)
        message = f"Mentor {first_name} {last_name} has been created."
        return redirect(url_for('view_mentors'))

@app.route("/mentors/update/<mentor_id>", methods=["GET", "POST"])
@login_required
def edit_mentor(mentor_id):
    if session.get('user_role_id',0) != 1 and session.get('userid',0) != mentor_id:
        return redirect(url_for('load_dashboard'))
    if request.method == "GET":
        mentor = mentor_model.get_mentor(mentor_id)
        mentor_categories = mentoring_categories_model.get_mentor_mentoring_categories(mentor_id)
        mentor_category_ids = []
        for category in mentor_categories:
            mentor_category_ids.append(category[0])

        return render_template("mentor/update.html", mentor=mentor, mentor_categories=','.join(map(str, mentor_category_ids)))
    else:
        # Get a list of category ids selected
        if (request.form['selectedCategoryIds']):
            new_category_ids = [int(x) for x in request.form['selectedCategoryIds'].split(",")]
        else:
            new_category_ids = []

        # Get the previously selected category ids
        old_category_ids = mentoring_categories_model.get_mentor_mentoring_categories(mentor_id)
        old_mentor_category_ids = []
        for category in old_category_ids:
            old_mentor_category_ids.append(category[0])

        # Get the categories that are in the old but not in the new
        to_be_deleted = [category for category in old_mentor_category_ids if category not in new_category_ids]
        for category in to_be_deleted:
            mentoring_categories_model.delete_mentor_mentoring_category(mentor_id, category)

        # Get the categories that are in the new but not in the old
        to_be_added = [category for category in new_category_ids if category not in old_mentor_category_ids]
        for category in to_be_added:
            mentoring_categories_model.add_mentor_mentoring_category(mentor_id, category)

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        mentor_model.update_mentor(mentor_id, email, first_name, last_name)
        return redirect(url_for('view_mentors'))

@app.route("/mentors/delete/<mentor_id>")
@login_required
@admin_role_required
def delete_mentor(mentor_id):
    mentor_model.delete_mentor(mentor_id)
    return redirect(url_for('view_mentors'))

@app.route("/mentors")
@login_required
@admin_role_required
def view_mentors():
    return render_template("mentor/list.html")

@app.route("/mentors/get-all-mentors")
@login_required
@admin_role_required
def get_all_mentors():
    data = mentor_model.view_all_mentors()
    return data
