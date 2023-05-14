#from __main__ import app
from flask import Flask, request, render_template, session, redirect, url_for, Blueprint
from auth.auth import login_required

dashboard_controller_bp = Blueprint('dashboard_controller_bp',__name__)
@dashboard_controller_bp.route("/")
@login_required
def load_dashboard():
    """
        Loads dashboard. Displays appropriate dashboard based on role
        Return
            template dashboard view
    """
    if session['user_role_id'] == 2:
        return render_template("dashboard/mentor_dashboard.html", session=session)

    if session['user_role_id'] == 1:
        return render_template("dashboard/admin_dashboard.html", session=session)

    return redirect(url_for('auth_controller_bp.login'))

@login_required
@dashboard_controller_bp.route("/profile")
def view_profile():
    """
        Displays profile. Displays appropriate profile based on role
        Return
            template edit profile view
    """
    if session['user_role_id'] == 2:
        return redirect('/mentors/update/' + str(session['userid']))

    if session['user_role_id'] == 1:
        return redirect('/admins/update/' + str(session['userid']))

    return redirect(url_for('auth_controller_bp.login'))
