from __main__ import app
from flask import Flask, request, render_template, session, redirect

@app.route("/create-mentor", methods=["GET", "POST"])
def create_mentor():
	return render_template('mentor/create.html')

def update_mentor():
	pass

def delete_mentor():
	pass

def view_all_mentors():
	pass

def view_mentor():
	pass