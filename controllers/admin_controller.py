from __main__ import app
from flask import Flask, request, render_template, session, redirect, url_for, flash
import models.admin_model as admin_model
from helpers.password_helper import generate_random_password, hash_password_string
from auth.auth import login_required
from auth.authz import admin_role_required


@app.route("/admins/create", methods=["GET", "POST"])
@login_required
@admin_role_required
def create_admin():
    """
        Create an admin. 
        GET method displays create form.
        POST method creates admin using form data.
        Returns:
            template with create admin form view.
            redirect to list of admin view.
    """
    if request.method == "GET":
        return render_template('admin/create.html')
    else:
        # process form
        password = generate_random_password()
        hashed_password = hash_password_string(password)
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        admin_model.insert_admin(email,first_name, last_name, hashed_password)

        flash(f"Admin {first_name} {last_name} has been created.", 'success')
        return redirect(url_for('view_admins'))

@app.route("/admins/update/<admin_id>", methods=["GET", "POST"])
@login_required
@admin_role_required
def edit_admin(admin_id):
    """
        Edit an admin. 
        GET method displays update form.
        POST method updates admin profile using form data.
        Parameters:
            madmin_id : id of admin to update.
        Returns:
            template with edit admin form view.
            redirect to list of admins view.
    """
    if request.method == "GET":
        admin = admin_model.get_admin(admin_id)
        return render_template('admin/update.html', admin=admin)
    else:
        # process form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        admin_model.update_admin(admin_id, email, first_name, last_name)
        message = f"Admin {first_name} {last_name} has been updated."
        flash(message, 'success')
        return redirect(url_for('view_admins'))

@app.route("/admins")
@login_required
@admin_role_required
def view_admins():
    """
        View admins.
        Returns:
            template with list of admins view. 
    """
    return render_template("admin/list.html")

@app.route("/admins/get-all-admins")
@login_required
@admin_role_required
def get_all_admins():
    """
        Get a list of admins. 
        Used by list of admin view to populate table.
    """
    data = admin_model.view_all_admins()
    return data

@app.route("/admins/delete/<admin_id>")
@login_required
@admin_role_required
def delete_admin(admin_id):
    """
        Delete an admin.
        Parameters:
            admin : id of admin todelete
        Returns:
            redirect to list of admins view. 
    """
    admin = admin_model.get_admin(admin_id)
    admin_model.delete_admin(admin_id)

    flash(f"Admin {admin[2]} {admin[3]} has been deleted.", 'success')
    return redirect(url_for('view_admins'))