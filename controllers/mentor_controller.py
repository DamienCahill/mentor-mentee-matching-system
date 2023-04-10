from __main__ import app
from flask import Flask, request, render_template, session, redirect
from models.mentor_model import get_mentor
from models.mentoring_categories_model import (
    get_mentor_mentoring_categories,
    delete_mentor_mentoring_category,
    add_mentor_mentoring_category
)
import sys

@app.route("/create-mentor", methods=["GET", "POST"])
def create_mentor():
    return render_template('mentor/create.html')

@app.route("/update-mentor/<mentor_id>", methods=["GET", "POST"])
def update_mentor(mentor_id):
    if request.method == "GET":
        mentor = get_mentor(mentor_id)
        mentor_categories = get_mentor_mentoring_categories(mentor_id)
        mentor_category_ids = []
        for category in mentor_categories:
            mentor_category_ids.append(category[0])

        return render_template("mentor/update.html", mentor=mentor, mentor_categories=','.join(map(str, mentor_category_ids)))
    else:
        if (request.form['selectedCategoryIds']):
            new_category_ids = [int(x) for x in request.form['selectedCategoryIds'].split(",")]
        else :
            new_category_ids = []
        print("here", sys.stdout)
        print(f"new_category_ids:{new_category_ids}",sys.stdout)
        old_category_ids = get_mentor_mentoring_categories(mentor_id)
        old_mentor_category_ids = []
        for category in old_category_ids:
            old_mentor_category_ids.append(category[0])
        print(f"old_category_ids:{old_mentor_category_ids}",sys.stdout)
        to_be_deleted = [category for category in old_mentor_category_ids if category not in new_category_ids]
        print(f"to be deleted:{to_be_deleted}",sys.stdout)
        for category in to_be_deleted:
            delete_mentor_mentoring_category(mentor_id, category)
        to_be_added = [category for category in new_category_ids if category not in old_mentor_category_ids]
        print(f"to be added:{to_be_added}",sys.stdout)
        for category in to_be_added:
            add_mentor_mentoring_category(mentor_id, category)
        return render_template("test.html", data=request.form)

def delete_mentor():
    pass

def view_all_mentors():
    pass

def view_mentor():
    pass