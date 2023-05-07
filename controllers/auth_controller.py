from __main__ import app
from flask import Flask, request, render_template, session, redirect
from models.auth_model import fetch_user_from_credentials, fetch_user_details_as_dictionary_from_id
import hashlib

@app.route("/login", methods=["GET", "POST"])
def login():
    """
        Login attempt.
        GET method displays login form.
        POST method attempts to login using credentials submitted in form.
        Returns:
            template with login form.
            redirect to dashboard.
    """
    if request.method == "POST": # Login form submissions
        email = request.form["email"]
        password = hashlib.md5(request.form["password"].encode()).hexdigest()
        user_id = fetch_user_from_credentials(email, password)
        if user_id:
            # Password is correct, set session variable and redirect to homepage
            session["userid"] = user_id

            # Update the session to contain the users details
            if (user_details := fetch_user_details_as_dictionary_from_id(user_id)):
                for key, value in user_details.items():
                    session[key] = value
            return redirect("/")
        else:
            # Invalid email or password, show error message
            flash("Invalid email or password", "danger")
            return render_template("login.html")
    else: # View Login page request
        if "userid" in session:
            # User is already logged in, redirect to homepage
            return redirect("/")
        else:
            # User is not logged in, show login form
            return render_template("login.html")

@app.route("/logout")
def logout():
    """
        Log user out/Removes userid from the session.
        Returns:
            Redirect to login form
    """
    session.pop('userid', None)
    return redirect("/login")