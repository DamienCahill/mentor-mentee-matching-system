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

def update_mentoring_categories(mentor_id, new_category_ids):
	old_category_ids = get_mentor_mentoring_categories(mentor_id)
	old_mentor_category_ids = []
	for category in mentor_categories:
		old_mentor_category_ids.append(category[0])

	to_be_deleted = [category for category in old_mentor_category_ids if category not in new_category_ids]
	for category in to_be_deleted:
		delete_mentor_mentoring_category(mentor_id, category)
	to_be_added = [category for category in new_category_ids if category not in old_mentor_category_ids]
	for category in to_be_added:
		add_mentor_mentoring_category(mentor_id, category)




