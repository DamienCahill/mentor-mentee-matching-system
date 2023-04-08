from __main__ import app
from flask import Flask, request, render_template, session, redirect
from models.mentor_model import get_mentor

@app.route("/create-mentor", methods=["GET", "POST"])
def create_mentor():
	return render_template('mentor/create.html')

@app.route("/update-mentor/<mentor_id>", methods=["GET", "POST"])
def update_mentor(mentor_id):
	mentor = get_mentor(mentor_id)
	return render_template("mentor/update.html", mentor=mentor)

def delete_mentor():
	pass

def view_all_mentors():
	pass

def view_mentor():
	pass