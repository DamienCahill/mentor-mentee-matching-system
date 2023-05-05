from __main__ import app
from flask import Flask, request, render_template, session, redirect, url_for
import models.admin_model as admin_model
from helpers.password_helper import generate_random_password, hash_password_string
from auth.auth import login_required
from auth.authz import admin_role_required


@app.route("/admins/create", methods=["GET", "POST"])
@login_required
@admin_role_required
def create_admin():
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
        message = f"Admin {first_name} {last_name} has been created."
        return redirect(url_for('view_admins'))

@app.route("/admins/update/<admin_id>", methods=["GET", "POST"])
@login_required
@admin_role_required
def edit_admin(admin_id):
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
        session['successMessage'] = message
        return redirect(url_for('view_admins'))

@app.route("/admins")
@login_required
@admin_role_required
def view_admins():
    return render_template("admin/list.html")

@app.route("/admins/get-all-admins")
@login_required
@admin_role_required
def get_all_admins():
    data = admin_model.view_all_admins()
    return data

@app.route("/admins/delete/<admin_id>")
@login_required
@admin_role_required
def delete_admin(admin_id):
    admin = admin_model.get_admin(admin_id)
    admin_model.delete_admin(admin_id)
    message = f"Admin {admin[2]} {admin[3]} has been deleted."
    return redirect(url_for('view_admins'))