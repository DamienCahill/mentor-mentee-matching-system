from __main__ import app
from flask import Flask, request, render_template, session, redirect
from models.mentor_model import (
    get_mentor,
    view_all_mentors
)
from models.mentoring_categories_model import (
    get_mentor_mentoring_categories,
    delete_mentor_mentoring_category,
    add_mentor_mentoring_category
)
import sys

@app.route("/create-mentor", methods=["GET", "POST"])
def create_mentor():
    return render_template('mentor/create.html')

@app.route("/mentors/edit/<mentor_id>", methods=["GET", "POST"])
def update_mentor(mentor_id):
    if request.method == "GET":
        mentor = get_mentor(mentor_id)
        mentor_categories = get_mentor_mentoring_categories(mentor_id)
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
        old_category_ids = get_mentor_mentoring_categories(mentor_id)
        old_mentor_category_ids = []
        for category in old_category_ids:
            old_mentor_category_ids.append(category[0])

        # Get the categories that are in the old but not in the new
        to_be_deleted = [category for category in old_mentor_category_ids if category not in new_category_ids]
        for category in to_be_deleted:
            delete_mentor_mentoring_category(mentor_id, category)

        # Get the categories that are in the new but not in the old
        to_be_added = [category for category in new_category_ids if category not in old_mentor_category_ids]
        for category in to_be_added:
            add_mentor_mentoring_category(mentor_id, category)
        return render_template("test.html", data=request.form)

def delete_mentor():
    pass

@app.route("/mentors")
def view_mentors():
    return render_template("mentor/list.html")

@app.route("/get-all-mentors")
def get_all_mentors():
    data = view_all_mentors()
    return data
