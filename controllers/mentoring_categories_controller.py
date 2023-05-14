from flask import Flask, request, render_template, session, redirect, Blueprint
from models.mentoring_categories_model import (
    get_all_mentoring_categories, 
    get_mentor_mentoring_categories,
    delete_mentor_mentoring_category,
    add_mentor_mentoring_category
)
mentoring_categories_controller_bp = Blueprint('mentoring_categories_controller_bp',__name__)

@mentoring_categories_controller_bp.route("/mentoring-categories", methods=["GET"]) 
def all_mentoring_categories():
    return get_all_mentoring_categories()

@mentoring_categories_controller_bp.route('/mentoring-categories/<mentor_id>', methods=["GET"])
def mentor_mentoring_categories(mentor_id):
    return get_mentor_mentoring_categories(mentor_id)





