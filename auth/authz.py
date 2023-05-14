from functools import wraps
from flask import request, redirect, url_for, session, flash

def admin_role_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_role_id',0) != 1:
            flash("You do not have permission to view that page. You have been redirected.", 'danger')
            return redirect(url_for('dashboard_controller_bp.load_dashboard'))
        return f(*args, **kwargs)
    return decorated_function