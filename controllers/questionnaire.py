from __main__ import app
from flask import Flask, request, render_template, session
from auth.auth import login_required

@app.route("/questionnaire") 
def view_questionnaire():
	return render_template("questionnaire.html")

def submit_questionnaire():
	pass

def view_submitted_questionnaires():
	pass

def view_submitted_questionnaire():
	pass