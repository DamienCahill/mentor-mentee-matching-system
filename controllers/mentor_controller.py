from flask import Flask, request, render_template, session, redirect, url_for, flash, Blueprint
import models.mentor_model as mentor_model
import models.mentoring_categories_model as mentoring_categories_model
from helpers.password_helper import generate_random_password, hash_password_string
import sys
from auth.auth import login_required
from auth.authz import admin_role_required

mentor_controller_bp = Blueprint('mentor_controller_bp',__name__)

@mentor_controller_bp.route("/mentors/create", methods=["GET", "POST"])
@login_required
@admin_role_required
def create_mentor():
    """
        Create a mentor. 
        GET method displays create form.
        POST method creates mentor profile using form data.
        Returns:
            template with create mentor form view.
            redirect to list of mentors view.
    """
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
        flash(message, 'success')
        return redirect(url_for('mentor_controller_bp.view_mentors'))

@mentor_controller_bp.route("/mentors/update/<mentor_id>", methods=["GET", "POST"])
@login_required
def edit_mentor(mentor_id):
    """
        Edit a mentor. 
        GET method displays update form.
        POST method updates mentor profile using form data.
        Parameters:
            mentor_id : id of mentor to update.
        Returns:
            template with edit mentor form view.
            redirect to list of mentors view.
    """

    # Only allow editing if user is an admin or if it is their own profile.
    if session.get('user_role_id',0) != 1 and session.get('userid') != int(mentor_id):
        return redirect(url_for('dashboard_controller_bp.load_dashboard'))

    if request.method == "GET": # Display the edit form.
        mentor = mentor_model.get_mentor(mentor_id)
        mentor_categories = mentoring_categories_model.get_mentor_mentoring_categories(mentor_id)
        mentor_category_ids = []
        for category in mentor_categories:
            mentor_category_ids.append(category[0])

        return render_template("mentor/update.html", mentor=mentor, mentor_categories=','.join(map(str, mentor_category_ids)), session=session)
    else: # Handle the submission of the edit form
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

        # Get the categories that are in the old but not in the new and delete them
        to_be_deleted = [category for category in old_mentor_category_ids if category not in new_category_ids]
        for category in to_be_deleted:
            mentoring_categories_model.delete_mentor_mentoring_category(mentor_id, category)

        # Get the categories that are in the new but not in the old and add them to profile
        to_be_added = [category for category in new_category_ids if category not in old_mentor_category_ids]
        for category in to_be_added:
            mentoring_categories_model.add_mentor_mentoring_category(mentor_id, category)

        # Update the mentor details
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        mentor_model.update_mentor(mentor_id, email, first_name, last_name)

        # Create flash messages to display and redirect.
        if session.get('userid') == int(mentor_id): # Editing own profile
            flash(f"Your profile has been updated.", 'success')
            return redirect('/mentors/update/' + mentor_id)

        flash(f"Mentor {first_name} {last_name} has been updated.", 'success')
        return redirect(url_for('mentor_controller_bp.view_mentors'))

@mentor_controller_bp.route("/mentors/delete/<mentor_id>")
@login_required
@admin_role_required
def delete_mentor(mentor_id):
    """
        Delete a mentor.
        Parameters:
            mentor_id : id of mentor delete
        Returns:
            redirect to list of mentors view. 
    """
    # Store the mentor details in a local variable, then delete them from db.
    mentor = mentor_model.get_mentor(mentor_id)
    mentor_model.delete_mentor(mentor_id)

    # Create flash message and redirect.
    flash(f"Admin {mentor[2]} {mentor[3]} has been deleted.", 'success')
    return redirect(url_for('mentor_controller_bp.view_mentors'))

@mentor_controller_bp.route("/mentors")
@login_required
@admin_role_required
def view_mentors():
    """
        View mentors.
        Returns:
            template with list of mentors view. 
    """
    return render_template("mentor/list.html")

@mentor_controller_bp.route("/mentors/get-all-mentors")
@login_required
@admin_role_required
def get_all_mentors():
    """
        Get a list of mentors. 
        Used by list of mentor view to populate table.
    """
    data = mentor_model.view_all_mentors()
    return data

@mentor_controller_bp.route("/mentors/matches")
@login_required
@admin_role_required
def view_mentor_matches():
    """
        View mentor matches
        Returns:
            template with list of mentor matches view.
    """
    return render_template('mentor/mentor-matches-list.html')

@mentor_controller_bp.route("/mentors/profiles")
def view_mentors_profile():
    """
        View mentors.
        Returns:
            template with public list of mentors view. 
    """
    return render_template("mentor/list_public.html")

@mentor_controller_bp.route("/mentors/get-all-mentors-public")
def get_all_mentors_public():
    """
        Get a list of mentors. 
        Used by list of mentor view to populate table.
    """
    data = mentor_model.view_all_mentors()
    return data

@mentor_controller_bp.route("/mentors/profiles/<mentor_id>")
def view_mentors_profile_public(mentor_id):
    """
        View a mentors profile publicallu.
        Returns:
            template with public view of mentor profile. 
    """
    if request.method == "GET": # Display the edit form.
        mentor = mentor_model.get_mentor(mentor_id)
        mentor_categories = mentoring_categories_model.get_mentor_mentoring_categories(mentor_id)
        mentor_category_ids = []
        for category in mentor_categories:
            mentor_category_ids.append(category[0])

        return render_template("mentor/view_public.html", mentor=mentor, mentor_categories=','.join(map(str, mentor_category_ids)))