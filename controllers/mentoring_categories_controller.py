from __main__ import app
from models.mentoring_categories_model import (
    get_all_mentoring_categories, 
    get_mentor_mentoring_categories,
    delete_mentor_mentoring_category,
    add_mentor_mentoring_category
)

@app.route("/mentoring-categories", methods=["GET"]) 
def all_mentoring_categories():
    return get_all_mentoring_categories()

@app.route('/mentoring-categories/<mentor_id>', methods=["GET"])
def mentor_mentoring_categories(mentor_id):
    return get_mentor_mentoring_categories(mentor_id)





