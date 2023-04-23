from __main__ import app
from flask import Flask, request, render_template, session, redirect
from auth.auth import login_required

@app.route("/")
@login_required
def load_dashboard():
	if session['user_role_id'] == 2:
		return render_template("dashboard/mentor_dashboard.html", session=session)

	if session['user_role_id'] == 1:
		return render_template("dashboard/admin_dashboard.html", session=session)

	return redirect(url_for('login'))

