from __main__ import app
from flask import Flask, request, render_template, session, redirect
from models.mentor_model import get_mentor
from models.admin_model import (
    view_all_admins,
    insert_admin,
    get_admin,
    update_admin
)
from helpers.password_helper import generate_random_password, hash_password_string

@app.route("/admins/create", methods=["GET", "POST"])
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
        insert_admin(email,first_name, last_name, hashed_password)
        message = f"Admin {first_name} {last_name} has been created. Password is {password}"
        return render_template('admin/list.html', message=message)

@app.route("/admins/update/<admin_id>", methods=["GET", "POST"])
def edit_admin(admin_id):
    if request.method == "GET":
        admin = get_admin(admin_id)
        return render_template('admin/update.html', admin=admin)
    else:
        # process form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        update_admin(admin_id, email, first_name, last_name)
        message = f"Admin {first_name} {last_name} has been updated."
        return render_template('admin/list.html', message=message)


@app.route("/admins")
def view_admins():
    return render_template("admin/list.html")

@app.route("/get-all-admins")
def get_all_admins():
    data = view_all_admins()
    return data

def delete_admin():
    pass